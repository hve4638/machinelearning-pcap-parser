import sys
from imglib import *;

# getsize.py [경로] [파일명(prefix)] [begin index] [end index]

target_dir = sys.argv[1]
fname_prefix = sys.argv[2]
beginindex = int(sys.argv[3])
endindex = int(sys.argv[4])

if not target_dir.endswith("/"):
    target_dir += "/"

target = []
for i in range(beginindex, endindex):
    target.append(f"{fname_prefix}{i}")

for i, fname in enumerate(target):
    print(f"{i}, ", len(read_binary_file(f"{target_dir}{fname}")))

    continue
    binary_data = d2(read_binary_file(f"packets/{fname}"), 40)
    binary_data = padding(binary_data, 40, 40)

    #checkarr(binary_data)
    save_binary_as_image(f'results/{fname}.png', binary_data)
