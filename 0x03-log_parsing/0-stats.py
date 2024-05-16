#!/usr/bin/python3
"""
0-stats.py
"""

import sys
import signal


# Initialize global variables
total_file_size = 0
status_codes_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
}
line_count = 0


def print_statistics():
    """Prints the accumulated statistics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interruption signal (CTRL + C)"""
    print_statistics()
    sys.exit(0)


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read from standard input line by line
for line in sys.stdin:
    line_count += 1
    try:
        # Parse the line
        parts = line.split()
        ip_address = parts[0]
        date = parts[3] + " " + parts[4]
        request = parts[5] + " " + parts[6] + " " + parts[7]
        status_code = int(parts[8])
        file_size = int(parts[9])

        # Validate the request format
        if request != '"GET /projects/260 HTTP/1.1"':
            continue

        # Update the total file size
        total_file_size += file_size

        # Update the status code count
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

    except (IndexError, ValueError):
        # Skip lines that do not match the format
        continue

    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print_statistics()

    # Print final statistics after processing all input lines
    print_statistics()
