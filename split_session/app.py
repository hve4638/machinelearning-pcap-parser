import sys, re, json
import csv
import pcapjson
from sessionsplit import *

s = Sessions()

def on_parse(data:map):
    addrs = getaddr(data)

    if not addrs:
        return
    skey = orderkey(*addrs)
    print(skey)
    
    s.addpkt(skey, data)

def on_error(data:map, exception:Exception, number:int):
    print("error")
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        print("Using")
        print(f"  {sys.argv[0]} [TargetFile] [OutputFile]")
        exit(-1)

    pcapjson.parse(target, on_parse, on_error, unhandle_error=True)

    # print(s.getsessions())
    print(len(s.getsessions()))