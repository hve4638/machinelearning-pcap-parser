import sys
from mllib import *;

# getsize.py [경로] [파일명(prefix)] [range] []

target_dir = to_dirpath(sys.argv[1])
fname_prefix = sys.argv[2]
st, ed = to_numrange(sys.argv[3])

target = []
for i in range(st, ed):
    target.append(f"{fname_prefix}{i}")

for i, fname in enumerate(target):
    length = len(read_binary_file(f"{target_dir}{fname}"))
    print(f"{i}, ", length)

    continue
    binary_data = d2(read_binary_file(f"packets/{fname}"), 40)
    binary_data = padding(binary_data, 40, 40)

    #checkarr(binary_data)
    save_binary_as_image(f'results/{fname}.png', binary_data)
