import sys
from mllib import *;

# toimg.py [경로] [파일명(prefix)] [인덱스범위] [저장경로]

target_dir = to_dirpath(sys.argv[1])
fname_prefix = sys.argv[2]
beginindex, endindex = to_numrange(sys.argv[3])
dest_dir = to_dirpath(sys.argv[4])

target = []
for i in range(beginindex, endindex):
    target.append(f"{fname_prefix}{i}")

for i, fname in enumerate(target):
    binary_data = d2(read_binary_file(f"{target_dir}{fname}"), 40)
    binary_data = arr_padding(binary_data, 40, 40)
    binary_data = arr_truncate(binary_data, 40, 40)

    save_binary_as_image(f'{dest_dir}{fname}.png', binary_data)
