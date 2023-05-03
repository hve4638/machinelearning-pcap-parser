import sys
import csv
import pcapjson

if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    target = "dataset/IoT Environment Dataset/[Normal]All_IoTs.json"

headers = pcapjson.Headers()
headers += ["TimeDelta", "timedelta"]
headers += ["Time", "time"]
headers += ["Source", "src"]
headers += ["Destination", "dest"]
headers += ["Length", "length", "len"]
headers += ["rule"]

rows = []
def on_parse(data:map):
    contents = headers.specifier()
    
    layers = data["_source"]["layers"]
    contents["timedelta"] = layers["frame"]["frame.time_delta"]
    contents["time"] = layers["frame"]["frame.time_relative"]

    if "ip" in layers and layers["ip"]["ip.version"] == "4":
        contents["src"] = layers["ip"]["ip.src_host"]
        contents["dest"] = layers["ip"]["ip.dst_host"]
    else:
        try:
            contents["src"] = layers["wlan"]["wlan.addr"]
            contents["dest"] = layers["wlan"]["wlan.ra"]
        except:
            contents["src"] = ""
            contents["dest"] = ""
        
    contents["length"] = layers["frame"]["frame.len"]

    if "frame.coloring_rule.name" in layers["frame"]:
        contents["rule"] = layers["frame"]["frame.coloring_rule.name"]
    else:
        contents["rule"] = layers["frame"]["frame.protocols"]

    rows.append(contents)

def on_error(data:map, exception:Exception, number:int):
    pass

#target = "example.json"
pcapjson.parse(target, on_parse, on_error)  
with open("output.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers.row)

    for row in rows:
        writer.writerow(row.row)
