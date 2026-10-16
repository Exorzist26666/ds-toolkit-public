@echo off
title DS Toolkit entfernen
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0uninstall.ps1"
