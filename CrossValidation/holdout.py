# Usage:
# holdout.py [대상파일] [비율] [train output] [test output] [noheader]

# 예시
# > holdout.py target.csv 7:3 train.csv test.csv

import sys
import math

target = sys.argv[1]
ratio  = sys.argv[2]
dest_train = sys.argv[3]
dest_test = sys.argv[4]
noheader = int(len(sys.argv) > 5)

a, b = ratio.split(":")
a = int(a)
b = int(b)
s = a+b
#print(a, b)
#print(noheader)

lines = []
with open(target, "r", encoding='utf-8') as f:
    lines = f.readlines()

if noheader:
    header = []
else:
    header = lines[0]
    lines = lines[1:]

length = len(lines)

train_len = math.ceil(length * a / s)
#test_len = length * math.floor(b/s)

with open(dest_train, "w", encoding="utf-8") as f:
    f.write(header)
    for line in lines[:train_len]:
        f.write(line)
with open(dest_test, "w", encoding="utf-8") as f:
    f.write(header)
    for line in lines[train_len:]:
        f.write(line)