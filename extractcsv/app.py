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
headers += ["No", "no"]
headers += ["TimeDelta", "timedelta"]
headers += ["Port", "port"]
headers += ["Length", "length", "len"]
headers += ["SYN", "syn"]
headers += ["ACK", "ack"]
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
    contents["no"] = layers["frame"]["frame.number"]
    if "tcp.flags_tree" in layers["tcp"]:
        contents["syn"] = layers["tcp"]["tcp.flags_tree"]["tcp.flags.syn"]
        contents["ack"] = layers["tcp"]["tcp.flags_tree"]["tcp.flags.ack"]
    else:
        contents["syn"] = 0
        contents["ack"] = 0

    rows.append(contents)

count = 0;
def on_error(data:map, exception:Exception, number:int):
    global count
    count += 1

    try:
        frame = data['_source']['layers']['frame']
        number = frame["frame.number"]
        time_relative = frame["frame.time_relative"]
        print(f'  - more (number: {number}, time_relative: {time_relative})', file=sys.stderr)
    except Exception as ex:
        print(f'  - unknown : {ex}', file=sys.stderr)
    

#target = "example.json"
pcapjson.parse(target, on_parse, on_error)  

print(rcount)
print(count)

with open(output_file, "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers.row)

    for row in rows:
        writer.writerow(row.row)
