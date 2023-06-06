import sys
from mllib import *;

# toimg.py [경로] [prefix] [인덱스범위] [저장경로]

target_dir = to_dirpath(sys.argv[1])
fname_prefix = sys.argv[2]
#fname_suffix = sys.argv[3]
numrange = sys.argv[3]
dest_dir = to_dirpath(sys.argv[4])

target = get_fname_in_dir(target_dir, fname_prefix, "", numrange)

for i, fname in enumerate(target):
    print(f"Find: {fname}")