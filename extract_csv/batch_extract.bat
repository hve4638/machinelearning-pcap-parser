@echo off

echo extract NormalTCP
python .\extracttocsv.py .\dataset\NormalTCP.json .\mid\NormalMid.csv
echo extract PortScanTCP
python .\extracttocsv.py .\dataset\PortScanTCP.json .\mid\PortScanMid.csv