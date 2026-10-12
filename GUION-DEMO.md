# Demo: un equipo de subagentes para desarrollo de software

**Duración:** ~25 min · **Herramienta:** Claude Code · **Lenguaje:** Python 3 (sin dependencias)

## Estructura

```
.claude/
  agents/
    revisor-codigo.md     → solo lectura: encuentra bugs y problemas de seguridad
    generador-tests.md    → escribe y ejecuta pruebas (no toca el código)
    depurador.md          → corrige el código (no toca las pruebas)
    documentador.md       → genera el README (modelo haiku, más barato)
  skills/
    flujo-calidad/        → orquesta a los 4 subagentes en orden
proyecto-demo/notas.py    → sistema de notas con bugs plantados
reiniciar-demo.ps1        → vuelve todo al estado inicial
```

## Bugs plantados (no mostrar a los estudiantes hasta el final)

| # | Función | Bug | Tipo |
|---|---|---|---|
| 1 | `calcular_promedio` | Lista vacía → `ZeroDivisionError` | Caso borde |
| 2 | `nota_final` | Prácticas pesan 0.3 (suma 110%) | Lógica |
| 3 | `estado` | `>` en vez de `>=`: con 51 reprueba | Valor límite |
| 4 | `validar_nota` | Acepta notas mayores a 100 | Validación |
| 5 | `buscar_estudiante` | SQL con f-string → inyección SQL | Seguridad |
| 6 | `ADMIN_PASSWORD` | Contraseña escrita en el código | Seguridad |
| 7 | `mejores_estudiantes` | Ordena de menor a mayor | Lógica |
| 8 | `reporte_*` | Código duplicado y mismo bug del `>` | Mantenibilidad |

## Antes de la clase

1. Ejecuta `./reiniciar-demo.ps1`.
2. Abre Claude Code en `C:\UPB\subajentes`.
3. Ensaya la demo una vez completa y reinicia otra vez.

## Guion

### Parte 1: ¿Qué es un subagente? (5 min)
Abre `.claude/agents/revisor-codigo.md` y explica las tres partes del frontmatter:
- `description` → el agente principal la lee para decidir **cuándo** delegar.
- `tools` → qué **puede** hacer (el revisor no puede escribir).
- `model` → cuánto **cuesta** y qué tan rápido es (comparar con `documentador`, que usa haiku).

### Parte 2: El programa "funciona" (2 min)
```
cd proyecto-demo
python notas.py
```
Pregunta a la clase: *"Con 20/20/40/20%, ¿la nota final de 80, 70, 90, 100 debería ser 96?"* (lo correcto es 86)
y *"¿Debería aprobar alguien con 51?"*

### Parte 3: Subagentes uno por uno (8 min)
Escribe en Claude Code:

1. `Usa el subagente generador-tests para probar proyecto-demo/notas.py`
   → Aparecen pruebas en rojo ❌. Señala que **no tocó el código**.
2. `Usa el revisor-codigo para revisar proyecto-demo/notas.py`
   → Encuentra la inyección SQL y la contraseña, cosas que las pruebas no ven.
   **Mensaje clave:** tests y revisión se complementan.
3. `Usa el depurador para corregir los fallos encontrados`
   → Las pruebas pasan a verde ✅.

### Parte 4: El pipeline completo (5 min)
Reinicia con `./reiniciar-demo.ps1` y escribe:

`/flujo-calidad`

Señala que el agente principal **orquesta**: los subagentes no se hablan entre sí.
Él le pasa a cada uno el resultado del anterior. El revisor y el generador de tests
pueden correr **en paralelo**.

### Parte 5: Preguntas para la clase (5 min)
- ¿Por qué el `generador-tests` no puede modificar `notas.py`? *(Si pudiera, haría trampa: cambiaría el código para que las pruebas pasen.)*
- ¿Por qué separar `depurador` y `generador-tests` en vez de un solo agente? *(Separación de responsabilidades, como en un equipo real: QA vs desarrollo.)*
- ¿Qué subagente agregarían ustedes? *(Ideas: arquitecto, revisor de rendimiento, generador de commits.)*

### Parte 6: Lo mismo en Codex y OpenCode (versatilidad)
Los mismos 4 subagentes existen para las tres herramientas. **La idea es la misma, cambia el formato.**

| | Claude Code | Codex | OpenCode |
|---|---|---|---|
| Carpeta de agentes | `.claude/agents/*.md` | `.codex/agents/*.toml` | `.opencode/agents/*.md` |
| Formato | Markdown + frontmatter | TOML | Markdown + frontmatter (`mode: subagent`) |
| Instrucciones | Cuerpo del `.md` | `developer_instructions` | Cuerpo del `.md` |
| Permisos | `tools: Read, Grep...` (lista blanca) | `sandbox_mode: read-only / workspace-write` | `permission: edit/bash: allow/ask/deny` |
| Modelo | `model: haiku` | `model = "gpt-6-luna"` + `model_reasoning_effort` | `model: proveedor/modelo` |
| Invocar | Automático por `description` o "usa el subagente X" | **Solo si lo pides**: "usa el agente revisor-codigo" | `@revisor-codigo` o automático |
| Flujo completo | `/flujo-calidad` (`.claude/skills/`) | `$flujo-calidad` (`.agents/skills/`) | `/flujo-calidad` (`.opencode/commands/`) |

Puntos para comentar:
- **Skills = estándar abierto:** el mismo `SKILL.md` funciona en las tres (OpenCode lee `.claude/skills/` y `.agents/skills/`).
- **Codex no delega solo:** hay que pedirle explícitamente que use los agentes.
- **Codex no tiene lista de herramientas:** controla con un *sandbox* (solo lectura o escritura en el proyecto).
- **OpenCode permite permisos por comando:** `"python *": allow` y el resto `ask`. Es más fino que Claude Code.

## Ejercicio para los estudiantes

Crear un subagente `revisor-rendimiento` en `.claude/agents/` que:
- Solo tenga herramientas de lectura.
- Busque bucles innecesarios y código duplicado.
- Proponga una versión más eficiente de `reporte_aprobados` y `reporte_reprobados`.
