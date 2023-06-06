import sys
from mllib import *;

# tonp3d.py [경로] [파일명(prefix)] [인덱스범위] [저장경로]

target_dir = to_dirpath(sys.argv[1])
fname_prefix = sys.argv[2]
numrange = to_numrange(sys.argv[3])
dest_dir = sys.argv[4]

target = get_fname_in_dir(dir, fname_prefix, "", numrange)

binary_data_ls = []
for i, fname in enumerate(target):
    binary_data = d2(read_binary_file(f"{target_dir}{fname}"), 40)
    binary_data = arr_padding(binary_data, 40, 40)
    binary_data = arr_truncate(binary_data, 40, 40)
    binary_data_ls.append(binary_data)

result_np = np.array(binary_data_ls)
np.save(f'{dest_dir}', result_np)