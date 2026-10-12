---
name: flujo-calidad
description: Ejecuta el pipeline completo de calidad de software (tests → revisión → corrección → documentación) usando los subagentes del proyecto. Úsala cuando pidan "flujo de calidad", "pipeline completo" o "revisa y arregla todo".
---

Coordina a los subagentes EN ORDEN. Tú eres el orquestador: los subagentes no se llaman entre sí,
tú le pasas a cada uno lo que necesita del anterior.

1. **generador-tests**: que cree y ejecute pruebas para `proyecto-demo/notas.py`.
2. **revisor-codigo**: que revise `proyecto-demo/notas.py` (puedes lanzarlo EN PARALELO con el paso 1,
   porque no depende de él).
3. **depurador**: pásale el resumen de fallos del paso 1 Y los 🔴/🟡 del paso 2. Que los corrija.
4. Si después del paso 3 todavía fallan pruebas, vuelve a llamar al depurador una vez más con esos fallos.
5. **documentador**: que genere el README.

Al final, muestra una tabla resumen:
| Etapa | Subagente | Resultado |
y el antes/después: cuántas pruebas fallaban al inicio y cuántas al final.
