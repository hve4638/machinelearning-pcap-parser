import sys
import csv
import pcapjson

if len(sys.argv) > 2:
    target = sys.argv[1]
    output_file = sys.argv[2]
else:
    print("Using")
    print(f"  {sys.argv[0]} [TargetFile] [OutputFile]")
    exit(-1)

headers = pcapjson.Headers()
headers += ["TimeDelta", "timedelta"]
headers += ["Length", "length", "len"]
headers += ["Port", "port"]
#headers += ["Attack", "attack"]
#headers += ["Time", "time"]
#headers += ["Source", "src"]
#headers += ["Destination", "dest"]

#headers += ["rule"]

rcount = 0
rows = []
def on_parse(data:map):
    global rcount
    contents = headers.specifier()
    rcount += 1
    layers = data["_source"]["layers"]
    contents["timedelta"] = layers["frame"]["frame.time_delta"]
    #contents["time"] = layers["frame"]["frame.time_relative"]
    
    contents["port"] = layers["tcp"]["tcp.dstport"]
    contents["length"] = layers["frame"]["frame.len"]
    #contents["attack"] = "0"

    rows.append(contents)

count = 0;

def on_error(data:map, exception:Exception, number:int):
    global count
    count += 1
    

#target = "example.json"
pcapjson.parse(target, on_parse, on_error)  

print(rcount)
print(count)

with open(output_file, "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers.row)

    for row in rows:
        writer.writerow(row.row)
