import sys
from imglib import *;

# toimg.py [경로] [파일명(prefix)] [begin index] [end index] [저장경로]

target_dir = sys.argv[1]
fname_prefix = sys.argv[2]
beginindex = int(sys.argv[3])
endindex = int(sys.argv[4])
dest_dir = sys.argv[5]

if not target_dir.endswith("/"):
    target_dir += "/"
if not dest_dir.endswith("/"):
    dest_dir += "/"

target = []
for i in range(beginindex, endindex):
    target.append(f"{fname_prefix}{i}")

for i, fname in enumerate(target):
    binary_data = d2(read_binary_file(f"{target_dir}{fname}"), 40)
    binary_data = padding(binary_data, 40, 40)

    save_binary_as_image(f'{dest_dir}{fname}.png', binary_data)
