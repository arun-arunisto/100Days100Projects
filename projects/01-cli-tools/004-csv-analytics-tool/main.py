from utilities import *
import time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV Analytics tool")
    parser.add_argument("file", help="Path to CSV file")

    args = parser.parse_args()
    time.sleep(1)
    print(BANNER)
    time.sleep(1)
    analyze_csv(args.file)
    