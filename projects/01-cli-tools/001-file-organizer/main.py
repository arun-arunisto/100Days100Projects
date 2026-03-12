from utilities import *


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files by their types")
    parser.add_argument("path", help="Directory to organize")
    args = parser.parse_args()
    time.sleep(2)
    print(BANNER)
    time.sleep(2)
    print(f"Organizing files in: {args.path}\nLoading...")
    time.sleep(2)
    organize(args.path)