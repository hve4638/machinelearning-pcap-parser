import re
import sys

# extracttobinary.py [입력파일] [출력파일]

h = re.compile(r"^([a-f0-9]+)\b([a-f0-9]{2}\b){,16}.*$", flags=re.MULTILINE)
w = re.compile(r"([a-f0-9]{2})", flags=re.MULTILINE)

def savebin(fname, data):
    with open(fname, "wb") as f:
        for value in data:
            f.write(bytes([value]))
count = 0
binary = []
with open(sys.argv[1], "r", encoding = "utf-16") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == "":
            if binary:
                savebin(f"{sys.argv[2]}{count}", binary);
                binary = []
                count+=1;
        if g := h.match(line):
            for i in w.finditer(line[6:54]):
                binary.append(int(i.group(0), 16));

if binary:
    savebin(f"{sys.argv[2]}{count}", binary);
    binary = []
    count += 1;
        