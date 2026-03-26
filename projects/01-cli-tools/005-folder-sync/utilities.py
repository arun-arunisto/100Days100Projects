# importing packages
import os
import shutil
import argparse

BANNER = r"""
              ._   .  .         
 __  .._  _.  |, _ | _| _ ._. __
_) \_|[ )(_.  | (_)|(_](/,[  _) 
   ._|     created by: arunisto                  
"""

def sync_folders(src, dst):

    # Handle single file sync
    if os.path.isfile(src):
        os.makedirs(dst, exist_ok=True)
        dst_file = os.path.join(dst, os.path.basename(src))
        if not os.path.exists(dst_file) or os.path.getmtime(src) > os.path.getmtime(dst_file):
            shutil.copy2(src, dst_file)
            print(f"[COPIED] {src}")
        else:
            print(f"[SKIPPED] {src} (already up to date)")
        return

    if not os.path.exists(dst):
        os.makedirs(dst)

    for root, dirs, files in os.walk(src):
        rel_path = os.path.relpath(root, src)
        target_dir = os.path.join(dst, rel_path)
        os.makedirs(target_dir, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(target_dir, file)

            if not os.path.exists(dst_file):
                shutil.copy2(src_file, dst_file)
                print(f"[NEW] {src_file}")
            
            else:
                src_mtime = os.path.getmtime(src_file)
                dst_mtime = os.path.getmtime(dst_file)

                if src_mtime > dst_mtime:
                    shutil.copy2(src_file, dst_file)
                    print(f"[UPDATED] {src_file}")
