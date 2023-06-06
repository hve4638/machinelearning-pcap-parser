import sys
import csv
import pcapjson

# Info 자연어 기반으로 ACK 여부 확인, Attack 라벨 추가

if len(sys.argv) > 2:
    target_file = sys.argv[1]
    output_file = sys.argv[2]
    is_attack = sys.argv[3]
else:
    print("Using")
    print(f"  {sys.argv[0]} [TargetFile] [OutputFile] [IsAttack]")
    exit(-1)

with open(target_file, "r", encoding="utf-8", newline='') as f:
    csv_reader = csv.reader(f)
    rows = list(csv_reader)
    index = rows[0].index("Info")
    rows[0].append("ATTACK")
    
    rows[0][index] = "ACK"
    for i, row in enumerate(rows):
        if i == 0:
            continue
        
        info = rows[i][index]
        rows[i].append(is_attack)
        if "ACK" in info:
            rows[i][index] = "1";
        else:
            rows[i][index] = "0";

with open(output_file, "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)

    for row in rows:
        writer.writerow(row)
