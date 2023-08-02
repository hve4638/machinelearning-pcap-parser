@echo off
setlocal enabledelayedexpansion

set /p input=input(without ext): 

python .\extractcsv\app.py .\input\%input%.json .\tmp\%input%.csv
python .\CrossValidation\holdout.py .\tmp\%input%.csv 7:3 .\output\%input%_train7.csv .\output\%input%_test3.csv
python .\CrossValidation\holdout.py .\tmp\%input%.csv 8:2 .\output\%input%_train8.csv .\output\%input%_test2.csv
python .\CrossValidation\holdout.py .\tmp\%input%.csv 9:1 .\output\%input%_train9.csv .\output\%input%_test1.csv

