# DS Toolkit - Deinstallation (Einstellungen bleiben erhalten)
param([string]$appdata = $env:APPDATA)
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Start-Process powershell -Verb RunAs -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$($MyInvocation.MyCommand.Path)`" -appdata `"$appdata`"" -Wait
    exit
}
$fusion = Join-Path $appdata "Blackmagic Design\DaVinci Resolve\Support\Fusion"
$tk = Join-Path $appdata "DS-Toolkit"
$items = @(
    (Join-Path $fusion "Scripts\Utility\DS Toolkit.py"),
    (Join-Path $fusion "Templates\Edit\Titles\DS Toolkit"),
    (Join-Path $fusion "Templates\Edit\Effects\DS Toolkit"),
    (Join-Path $env:ProgramData "Blackmagic Design\DaVinci Resolve\Support\LUT\DS Toolkit"),
    (Join-Path $tk "lib"),
    (Join-Path $tk "assets"),
    (Join-Path $tk "cache")
)
foreach ($i in $items) { if (Test-Path $i) { Remove-Item $i -Recurse -Force; Write-Host "entfernt: $i" } }
Write-Host ""
Write-Host "DS Toolkit entfernt. Einstellungen liegen weiter in $tk\settings.json" -ForegroundColor Cyan
Read-Host "Enter zum Schliessen" | Out-Null
