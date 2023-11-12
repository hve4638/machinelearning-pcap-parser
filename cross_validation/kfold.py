import sys
import os

# kfold.py [target] [k] [dest] [noheader]
#
# example:
#    python kfold.py .\NormalTCP.csv 5 .\result\

def lssplit(ls, n):
    k, m = divmod(len(ls), n)
    return [ls[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]

target = sys.argv[1]
k = int(sys.argv[2])
dest_dir = sys.argv[3]
noheader = int(len(sys.argv) > 4)

dest_dir = dest_dir.replace("\\", "/")
if not dest_dir.endswith("/"):
    dest_dir += "/"

lines = []
with open(target, "r", encoding='utf-8') as f:
    lines = f.readlines()

if noheader:
    header = []
else:
    header = lines[0]
    lines = lines[1:]

klines = lssplit(lines, k)

file_fullname = os.path.basename(target)
file_name, file_ext = os.path.splitext(file_fullname)

for i in range(k):
    ls = []
    
    dest_train = f"{dest_dir}{file_name}_Train{i}.{file_ext}"
    with open(dest_train, "w", encoding="utf-8") as f:
        f.write(header)
        for j in range(k):
            if i != j:
                for line in klines[j]:
                    f.write(line)
    
    dest_test = f"{dest_dir}{file_name}_Test{i}.{file_ext}"
    with open(dest_test, "w", encoding="utf-8") as f:
        f.write(header)
        for line in klines[i]:
            f.write(line)