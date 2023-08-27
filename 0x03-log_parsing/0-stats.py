#!/usr/bin/python3
import sys
from collections import defaultdict

def print_statistics(stats):
    total_size = sum(stats.values())
    print(f"Total file size: File size: {total_size}")
    for status, count in sorted(stats.items()):
        print(f"{status}: {count}")

def main():
    stats = defaultdict(int)
    lines_processed = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 7:
                _, _, _, _, status, size = parts[0], parts[5], parts[6]
                if status.isdigit() and size.isdigit():
                    stats[status] += 1
                    lines_processed += 1
                    if lines_processed % 10 == 0:
                        print_statistics(stats)
            if lines_processed % 10 == 0:
                print_statistics(stats)
    except KeyboardInterrupt:
        print_statistics(stats)

if __name__ == "__main__":
    main()
