import sys
from mllib import *;

# toimg.py [경로] [파일명(prefix)] [인덱스범위] [저장경로]

target_dir = to_dirpath(sys.argv[1])
fname_prefix = sys.argv[2]
numrange = sys.argv[3]
dest_dir = to_dirpath(sys.argv[4])

def filter_call(packet_bytes):
    body = list(packet_get_body(packet_bytes))
    if len(body) < 225:
        return True
    else:
        return False

target = get_fname_in_dir(target_dir, fname_prefix, '', numrange)
os.makedirs(dest_dir, exist_ok=True)

total_contents = 0
passed_contents = 0
blocked_contents = 0
for i, fname in enumerate(target):
    source_fname = f"{target_dir}{fname}"
    dest_fname = f"{dest_dir}{fname}"

    total_contents += 1
    bpacket = bytes(read_binary_file(source_fname))
    if filter_call(bpacket):
        cp_file(source_fname, dest_fname)
        passed_contents += 1
    else:
        blocked_contents += 1

print(f"Total: {total_contents}")
print(f"Pass: {passed_contents}")
print(f"Block: {blocked_contents}")