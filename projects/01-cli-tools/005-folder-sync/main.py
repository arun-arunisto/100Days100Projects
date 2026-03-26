from utilities import *
import time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Folder Sync Tool")
    parser.add_argument("source", help="Source folder")
    parser.add_argument("destination", help="Destination folder")

    args = parser.parse_args()
    time.sleep(1)
    print(BANNER)
    time.sleep(1)
    sync_folders(args.source, args.destination)