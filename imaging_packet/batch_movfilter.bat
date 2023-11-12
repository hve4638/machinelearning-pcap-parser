:: raw 패킷데이터에서 일정 크기 내의 패킷만 분류후 복사
::
python .\movfilter.py .\contents\raw\normal\ bin * .\contents\filter\normal\
python .\movfilter.py .\contents\raw\portscan\ bin * .\contents\filter\portscan\