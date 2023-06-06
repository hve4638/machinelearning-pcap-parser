import os
import re

def to_dirpath(dir:str):
    dir = dir.replace('\\', '/')
    if not dir.endswith("/"):
        dir += "/"
    return dir

def to_numrange(arg):
    start, end = map(int, arg.split('-'))
    return start, end

def get_fname_in_dir(dir, prefix, suffix, numrange):
    target = []
    if numrange == '*':
        for fname in os.listdir(dir):
            if fname.startswith(prefix):
                target.append(fname)
    else:
        beginindex, endindex = to_numrange(numrange)
        for i in range(beginindex, endindex):
            target.append(f"{prefix}{i}{suffix}")

    return target