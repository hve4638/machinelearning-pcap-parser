import sys
from mllib import *;

# toimg.py [경로] [prefix] [suffix] [인덱스범위] [저장경로]

target_dir = to_dirpath(sys.argv[1])
fname_prefix = sys.argv[2]
fname_suffix = sys.argv[3]
numrange = sys.argv[4]
dest_dir = to_dirpath(sys.argv[5])

target = get_fname_in_dir(target_dir, fname_prefix, fname_suffix, numrange)

for i, fname in enumerate(target):
    bpacket = bytes(read_binary_file(f"{target_dir}{fname}"))
    body = packet_get_body(bpacket)

    binary_data = d2(list(body), 40)
    binary_data = arr_padding(binary_data, 40, 40)
    binary_data = arr_truncate(binary_data, 40, 40)
    print(f"{i},{len(body)}")
