# IMPORTS
import os
import shutil
import argparse
import time


BANNER = r"""                                                                           
 _____ _____ __    _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
|   __|     |  |  |   __|     | __  |   __|  _  |   | |     |__   |   __| __  |
|   __|-   -|  |__|   __|  |  |    -|  |  |     | | | |-   -|   __|   __|    -|
|__|  |_____|_____|_____|_____|__|__|_____|__|__|_|___|_____|_____|_____|__|__|
                                                    created by: arun arunisto
"""

# FILE Types
FILE_TYPES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".svg"],
    "documents":[".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "videos": [".mp4", ".avi", ".mkv", ".mov", ".webm"],
    "archives": [".zip", ".tar", ".gz", ".rar", ".7z", ".iso"]
}

def moving_to_folder(directory, folder, filename, file_path):
    # creating target folder path
    target = os.path.join(directory, folder)

    # creating target folder if it doesn't exist
    os.makedirs(target, exist_ok=True)

    # moving the file to the target folder
    shutil.move(file_path, os.path.join(target, filename))

    print(f"Moved {filename} to {folder}")


def organize(directory):
    for filename in os.listdir(directory):
        # file path
        file_path = os.path.join(directory, filename)

        # checking file path exists and is a file
        if os.path.isfile(file_path):
            # getting the file extension
            ext = os.path.splitext(filename)[1].lower()

            moved = False

            for folder, extensions in FILE_TYPES.items():
                # checking if the file extension matches any of the defined types
                if ext in extensions:
                    moving_to_folder(directory=directory, folder=folder, filename=filename, file_path=file_path)
                    # setting moved to true to indicate the file has been moved
                    moved = True
                    break
            
            # if the file doesn't match any folders we can move it to an "others" folder
            if not moved:
                moving_to_folder(directory=directory, folder="others", filename=filename, file_path=file_path)

