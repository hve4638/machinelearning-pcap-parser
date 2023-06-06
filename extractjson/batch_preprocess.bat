@echo off

echo process NormalTCP
python .\csvpreprocess.py .\mid\NormalMid.csv .\result\NormalTCP_ALL.csv 0
echo process PortScanTCP
python .\csvpreprocess.py .\mid\PortScanMid.csv .\result\PortScanTCP_ALL.csv 1