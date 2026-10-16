# DS Toolkit - Installation (Erstinstallation oder komplette Neuinstallation)
param([string]$appdata = $env:APPDATA, [string]$localappdata = $env:LOCALAPPDATA)
$ErrorActionPreference = "Continue"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$pkg = Join-Path $here "paket"

$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "Frage Admin-Rechte an (für die Color-Tools) ..." -ForegroundColor Yellow
    $args2 = "-NoProfile -ExecutionPolicy Bypass -File `"$($MyInvocation.MyCommand.Path)`" -appdata `"$appdata`" -localappdata `"$localappdata`""
    $p = Start-Process powershell -Verb RunAs -ArgumentList $args2 -PassThru -Wait
    exit
}

Write-Host ""
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host "   DS TOOLKIT für DaVinci Resolve Studio" -ForegroundColor Cyan
Write-Host "==============================================" -ForegroundColor Cyan
$ver = (Get-Content (Join-Path $pkg "manifest.json") -Raw | ConvertFrom-Json).version
Write-Host "Version: $ver"
Write-Host ""

if (Get-Process -Name "Resolve" -ErrorAction SilentlyContinue) {
    Write-Host "DaVinci Resolve läuft noch. Bitte Resolve schließen und Enter drücken." -ForegroundColor Yellow
    Read-Host | Out-Null
}

$fusion = Join-Path $appdata "Blackmagic Design\DaVinci Resolve\Support\Fusion"
$tk = Join-Path $appdata "DS-Toolkit"
$dctl = Join-Path $env:ProgramData "Blackmagic Design\DaVinci Resolve\Support\LUT\DS Toolkit"
$map = @{
    "scripts"   = (Join-Path $fusion "Scripts\Utility");
    "templates" = (Join-Path $fusion "Templates");
    "lib"       = (Join-Path $tk "lib");
    "assets"    = (Join-Path $tk "assets");
    "dctl"      = $dctl
}
foreach ($k in $map.Keys) {
    $src = Join-Path $pkg $k
    if (Test-Path $src) {
        New-Item -ItemType Directory -Force -Path $map[$k] | Out-Null
        Copy-Item -Path (Join-Path $src "*") -Destination $map[$k] -Recurse -Force
        Write-Host ("OK  " + $k.PadRight(10) + " -> " + $map[$k]) -ForegroundColor Green
    }
}

# Python 3 (Resolve braucht es für Python-Skripte) + numpy (Audio-Analyse)
Write-Host ""
Write-Host "Prüfe Python ..."
function Find-Python {
    $cands = @()
    $cmd = Get-Command py -ErrorAction SilentlyContinue
    if ($cmd) { $cands += $cmd.Source }
    $cands += Get-ChildItem -Path "$localappdata\Programs\Python\Python3*\python.exe", "$env:ProgramFiles\Python3*\python.exe" -ErrorAction SilentlyContinue | Sort-Object FullName -Descending | ForEach-Object { $_.FullName }
    foreach ($c in $cands) { if ($c -and (Test-Path $c)) { return $c } }
    return $null
}
$py = Find-Python
if (-not $py) {
    $wg = Get-Command winget -ErrorAction SilentlyContinue
    if ($wg) {
        Write-Host "Installiere Python 3.12 (dauert 1-2 Minuten) ..."
        winget install --id Python.Python.3.12 -e --scope machine --accept-source-agreements --accept-package-agreements --silent | Out-Null
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
        $py = Find-Python
    }
}
if ($py) {
    Write-Host "OK  Python ($py)" -ForegroundColor Green
    if ((Split-Path -Leaf $py) -eq "py.exe") { & $py -3 -m pip install --quiet numpy 2>$null } else { & $py -m pip install --quiet numpy 2>$null }
    if ($LASTEXITCODE -eq 0) { Write-Host "OK  numpy" -ForegroundColor Green } else { Write-Host "!   numpy konnte nicht installiert werden (Audio-Funktionen evtl. eingeschränkt)" -ForegroundColor Yellow }
} else {
    Write-Host "!   Python konnte nicht automatisch installiert werden." -ForegroundColor Yellow
    Write-Host "    Bitte Python 3 von https://www.python.org/downloads/ installieren (Haken bei 'Add python.exe to PATH')" -ForegroundColor Yellow
    Write-Host "    und danach INSTALL.bat noch einmal ausführen." -ForegroundColor Yellow
}

# ffmpeg (für Audio, Export und Effekte)
$ff = Get-Command ffmpeg -ErrorAction SilentlyContinue
$wingetFF = Join-Path $localappdata "Microsoft\WinGet\Links\ffmpeg.exe"
if ($ff -or (Test-Path $wingetFF)) {
    Write-Host "OK  ffmpeg" -ForegroundColor Green
} else {
    Write-Host "Installiere ffmpeg ..."
    $wg = Get-Command winget -ErrorAction SilentlyContinue
    if ($wg) {
        winget install --id Gyan.FFmpeg -e --accept-source-agreements --accept-package-agreements --silent | Out-Null
    }
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
    if ((Get-Command ffmpeg -ErrorAction SilentlyContinue) -or (Test-Path $wingetFF) -or (Get-ChildItem "$env:ProgramFiles\WinGet\Links\ffmpeg.exe" -ErrorAction SilentlyContinue)) {
        Write-Host "OK  ffmpeg" -ForegroundColor Green
    } else {
        Write-Host "!   ffmpeg konnte nicht automatisch installiert werden." -ForegroundColor Yellow
        Write-Host "    Bitte von https://www.gyan.dev/ffmpeg/builds/ laden oder in einer Eingabeaufforderung: winget install Gyan.FFmpeg" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "Fertig! Resolve starten -> Workspace > Scripts > DS Toolkit" -ForegroundColor Cyan
Write-Host ""
Read-Host "Enter zum Schliessen" | Out-Null
