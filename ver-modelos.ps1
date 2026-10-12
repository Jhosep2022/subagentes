# Muestra qué modelo usó cada subagente en la última sesión de Claude Code de este proyecto.
# Lee los registros (transcripts) que Claude Code guarda en ~/.claude/projects/.
$proyecto = "$env:USERPROFILE\.claude\projects\c--UPB-subajentes"
$sesion = Get-ChildItem $proyecto -Directory |
    Where-Object { Test-Path "$($_.FullName)\subagents" } |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1

if (-not $sesion) { Write-Host "Todavía no hay subagentes ejecutados."; exit }

$archivoPrincipal = "$proyecto\$($sesion.Name).jsonl"
$modeloPrincipal = (Select-String -Path $archivoPrincipal -Pattern '"model":"(claude-[^"]+)"' |
    Select-Object -Last 1).Matches.Groups[1].Value
Write-Host "`nAgente principal -> $modeloPrincipal`n"

Get-ChildItem "$($sesion.FullName)\subagents\*.meta.json" | ForEach-Object {
    $meta = Get-Content $_.FullName -Raw | ConvertFrom-Json
    $registro = $_.FullName -replace '\.meta\.json$', '.jsonl'
    $modelo = (Select-String -Path $registro -Pattern '"model":"(claude-[^"]+)"' |
        Select-Object -First 1).Matches.Groups[1].Value
    [PSCustomObject]@{ Subagente = $meta.agentType; Tarea = $meta.description; Modelo = $modelo }
} | Format-Table -AutoSize
