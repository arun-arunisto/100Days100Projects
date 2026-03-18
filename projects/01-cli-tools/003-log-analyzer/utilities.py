# importing necessary libraries
import re
import argparse
from collections import Counter


BANNER = r"""
  _      ____   _____          _   _          _  __     ______________ _____  
 | |    / __ \ / ____|   /\   | \ | |   /\   | | \ \   / /___  /  ____|  __ \ 
 | |   | |  | | |  __   /  \  |  \| |  /  \  | |  \ \_/ /   / /| |__  | |__) |
 | |   | |  | | | |_ | / /\ \ | . ` | / /\ \ | |   \   /   / / |  __| |  _  / 
 | |___| |__| | |__| |/ ____ \| |\  |/ ____ \| |____| |   / /__| |____| | \ \ 
 |______\____/ \_____/_/    \_\_| \_/_/    \_\______|_|  /_____|______|_|  \_\
                                                    created by: arun-arunisto
"""

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+).*"(?P<method>\S+)\s+(?P<path>\S+).*"\s+(?P<status>\d{3})'
)


def parse_log(file_path):
    ip_counter = Counter()
    path_counter = Counter()
    status_counter = Counter()

    total_requests = 0

    with open(file_path, "r") as f:
        for line in f:
            # checking for the match in the log lines
            match = LOG_PATTERN.search(line)

            # not matching the log line, skipping it
            if not match:
                continue

            # total requests
            total_requests += 1

            # counting the IP addresses, paths and status codes
            ip = match.group("ip")
            path = match.group("path")
            status = int(match.group("status"))

            ip_counter[ip] += 1
            path_counter[path] += 1
            status_counter[status] += 1
    
    return ip_counter, path_counter, status_counter, total_requests

def categorize_errors(status_counter):
    errors = {
        "4xx":0,
        "5xx":0
    }

    for status, count in status_counter.items():
        if 400 <= status < 500:
            errors["4xx"] += count
        elif 500 <= status < 600:
            errors["5xx"] += count
    
    return errors

def print_stats(ip_counter, path_counter, status_counter, total_requests, top_n, only_errors):
    
    print(f"\nTotal Requests: {total_requests}")

    if not only_errors:
        print("\nTop IP Addresses:")
        for ip, count in ip_counter.most_common(top_n):
            percent = (count/total_requests)*100
            print(f"{ip} → {count} ({percent:.2f}%)")
        
        print("\nTop Endpoints:")
        for path, count in path_counter.most_common(top_n):
            percent = (count/total_requests)*100
            print(f"{path} → {count} ({percent:.2f}%)")
        
    print("\nStatus Codes:")
    for status, count in status_counter.items():
        percent = (count/total_requests)*100
        print(f"{status} → {count} ({percent:.2f}%)")
    
    errors = categorize_errors(status_counter)
    print("\nError Summary:")
    print(f"4xx Errors → {errors['4xx']}")
    print(f"5xx Errors → {errors['5xx']}")


        


