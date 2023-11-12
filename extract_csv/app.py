import sys
import csv
import pcapjson
import re
from request_frequency import RequestFrequency
from synack import SynAck

if len(sys.argv) > 2:
    target = sys.argv[1]
    output_file = sys.argv[2]
else:
    print("Using")
    print(f"  {sys.argv[0]} [TargetFile] [OutputFile]")
    exit(-1)

rcount = 0
errcount = 0

headers = pcapjson.Headers()
headers += ["No", "no"]
headers += ["TimeDelta", "timedelta"]
headers += ["Time", "time"]
headers += ["Port", "port"]
headers += ["Length", "length", "len"]
headers += ["SYN", "syn"]
headers += ["ACK", "ack"]
#headers += ["Attack", "attack"]
headers += ["Source", "src"]
headers += ["Destination", "dst"]
headers += ["RequestFrequency", "requestfrequency"]
#headers += ["TimeCost", "timecost"]
#headers += ["rule"]

rf = RequestFrequency(time_interval=5)
sa = SynAck()

rows = []
def on_parse(data:map):
    global rcount
    rcount += 1

    contents = headers.specifier()
    layers = data["_source"]["layers"]

    time_relative = layers["frame"]["frame.time_relative"]

    contents["timedelta"] = layers["frame"]["frame.time_delta"]
    contents["time"] = time_relative
    contents["port"] = layers["tcp"]["tcp.dstport"]
    contents["length"] = layers["frame"]["frame.len"]
    contents["no"] = layers["frame"]["frame.number"]
    
    if "ip.addr" in layers["ip"]:
        src = layers["ip"]["ip.src_host"]
        dst = layers["ip"]["ip.dst_host"]

        contents["src"] = src
        contents["dst"] = dst
        contents["requestfrequency"] = rf.add(time_relative=time_relative, addr=src)
    else:
        contents["src"] = "Unknown"
        contents["dst"] = "Unknown"
        contents["requestfrequency"] = 0


    tc = "0.000000000"
    if "tcp.flags_tree" in layers["tcp"]:
        syn = layers["tcp"]["tcp.flags_tree"]["tcp.flags.syn"]
        ack = layers["tcp"]["tcp.flags_tree"]["tcp.flags.ack"]
        rst = layers["tcp"]["tcp.flags_tree"]["tcp.flags.reset"]
        contents["syn"] = syn
        contents["ack"] = ack
        if int(syn):
            sa.syn(src, dst, time_relative)
        if int(ack) or int(rst):
            tc = sa.ack(src, dst, time_relative)
    else:
        contents["syn"] = 0
        contents["ack"] = 0
    #contents["timecost"] = tc

    rows.append(contents)

def on_error(data:map, exception:Exception, number:int):
    global errcount
    errcount += 1

    try:
        frame = data['_source']['layers']['frame']
        number = frame["frame.number"]
        time_relative = frame["frame.time_relative"]
        sys.stderr.write(f'  - error (number: {number}, time_relative: {time_relative}) {type(exception)}: {exception}\n')
    except Exception as ex:
        print(f'  - unknown : {ex}', file=sys.stderr)

pcapjson.parse(target, on_parse, on_error)  

print(f"count : {rcount}")
print(f"error count: {errcount}")
print(f"save file as {output_file}")

with open(output_file, "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers.row)

    for row in rows:
        writer.writerow(row.row)
