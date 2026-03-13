from utilities import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find duplicate files in a directory")
    parser.add_argument("path", help="Path to the directory to scan for duplicate files")
    args = parser.parse_args()
    time.sleep(2)
    print(BANNER)
    time.sleep(2)
    duplicates = find_duplicates(args.path)
    print_duplicates(duplicates)