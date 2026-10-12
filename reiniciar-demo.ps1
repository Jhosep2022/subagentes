# Deja la demo como al inicio: código con bugs, sin tests ni README.
$raiz = $PSScriptRoot
Copy-Item "$raiz\.reset\notas.py" "$raiz\proyecto-demo\notas.py" -Force
Remove-Item "$raiz\proyecto-demo\tests" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$raiz\proyecto-demo\README.md" -Force -ErrorAction SilentlyContinue
Remove-Item "$raiz\proyecto-demo\__pycache__" -Recurse -Force -ErrorAction SilentlyContinue
Write-Host "Demo reiniciada."
