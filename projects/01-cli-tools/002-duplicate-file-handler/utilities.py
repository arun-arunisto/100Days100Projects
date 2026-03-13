import os
import hashlib
import shutil
import argparse
from collections import defaultdict
import time


BANNER = r"""
 :::====  :::  === :::====  :::      ::: :::===== :::====  :::==== :::=====          
 :::  === :::  === :::  === :::      ::: :::      :::  === :::==== :::               
 ===  === ===  === =======  ===      === ===      ========   ===   ======            
 ===  === ===  === ===      ===      === ===      ===  ===   ===   ===               
 =======   ======  ===      ======== ===  ======= ===  ===   ===   ========          
                                                                                    
 :::===== ::: :::      :::=====      :::===== ::: :::= === :::====  :::===== :::==== 
 :::      ::: :::      :::           :::      ::: :::===== :::  === :::      :::  ===
 ======   === ===      ======        ======   === ======== ===  === ======   ======= 
 ===      === ===      ===           ===      === === ==== ===  === ===      === === 
 ===      === ======== ========      ===      === ===  === =======  ======== ===  ===
                                                            created by: @arun-arunisto                           
"""

def file_hash(path):
    # Create a hash object
    hasher = hashlib.md5()

    # Open the file in binary mode and read it in chunks
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    
    return hasher.hexdigest()

# finding duplicates
def find_duplicates(directory):
    size_map = defaultdict(list)

    # step 1: grouping files by size
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)

            try:
                size = os.path.getsize(path)
                size_map[size].append(path)
            except OSError:
                pass
    
    hash_map = defaultdict(list)

    # step 2: hash only same-size files
    for size, files in size_map.items():
        if len(files) < 2:
            continue

        for path in files:
            try:
                h = file_hash(path)
                hash_map[h].append(path)
            except OSError:
                pass
    
    # step 3: filtering the real duplicates
    duplicates = {h: files for h, files in hash_map.items() if len(files) > 1}

    return duplicates

# printing duplicates
def print_duplicates(duplicates):
    if not duplicates:
        print("No duplicates found")
        return 
    
    print("\nDuplicates files found: \n")
    for files in duplicates.values():
        print(f"Duplicate group ({len(files)} files):")
        for f in files:
            print(f" {f}")
        
        print("-"*40)

