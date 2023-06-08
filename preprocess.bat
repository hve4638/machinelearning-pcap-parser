@echo off
setlocal enabledelayedexpansion

echo %1
echo %2
python .\extractcsv\app.py .\dataset\%1 .\result\%2

