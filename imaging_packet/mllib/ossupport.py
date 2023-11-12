import sys
import os
import shutil

def cp_file(source_path, destination_path):
    shutil.copy2(source_path, destination_path)
