from utilities import *
import time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log Analyzer CLI")

    parser.add_argument("file", help="Path to log file")
    parser.add_argument("--top", type=int, default=5, help="Top N results")
    parser.add_argument("--errors", action="store_true", help="Show only error stats")

    args = parser.parse_args()
    ip_counter, path_counter, status_counter, total_requests = parse_log(args.file)

    print(BANNER)
    time.sleep(1)
    print_stats(
        ip_counter,
        path_counter,
        status_counter,
        total_requests,
        args.top,
        args.errors
    )
