param(
    [switch]$SameWindow,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$backendPath = $repoRoot
$frontendPath = Join-Path $repoRoot "angular\frontend"
$portableNodePath = "C:\Users\ivivas\CodeWorkSpace\tools\node-v22\node-v22.23.3-win-x64"

if (-not (Test-Path $frontendPath)) {
    throw "No se encuentra el frontend en: $frontendPath"
}

if (Test-Path $portableNodePath) {
    $env:Path = "$portableNodePath;$env:Path"
}

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    throw "No se encontró 'uv' en PATH. Instala uv o abre una terminal con uv disponible."
}

if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
    throw @"
No se encontró 'npm' en PATH.
Opciones:
1) Instalar Node.js globalmente.
2) Usar Node portátil en: $portableNodePath
"@
}

$backendCmd = "cd `"$backendPath`"; uv run fastapi dev main.py"
$frontendCmd = "cd `"$frontendPath`"; npm start"

Write-Host "Backend:  $backendCmd" -ForegroundColor Cyan
Write-Host "Frontend: $frontendCmd" -ForegroundColor Cyan

if ($DryRun) {
    Write-Host "DryRun activo: no se han iniciado procesos." -ForegroundColor Yellow
    return
}

if ($SameWindow) {
    $backendProcess = Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", $backendCmd -PassThru
    Write-Host "Backend iniciado (PID: $($backendProcess.Id))." -ForegroundColor Green

    cd $frontendPath
    npm start
}
else {
    $backendProcess = Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", $backendCmd -PassThru
    $frontendProcess = Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", $frontendCmd -PassThru

    Write-Host "Backend iniciado (PID: $($backendProcess.Id))." -ForegroundColor Green
    Write-Host "Frontend iniciado (PID: $($frontendProcess.Id))." -ForegroundColor Green
    Write-Host "Abre http://localhost:4200 (front) y http://localhost:8000/docs (API)." -ForegroundColor Green
}
