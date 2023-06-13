#!/usr/bin/python3
"""Log parsing"""


import sys
import signal


def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

def print_metrics():
    print("Total file size: File size: {}".format(total_size))
    for status_code in sorted(status_codes):
        print("{}: {}".format(status_code, status_codes[status_code]))

signal.signal(signal.SIGINT, signal_handler)


total_size = 0
status_codes = {}

for i, line in enumerate(sys.stdin):
    parts = line.split()
    if len(parts) == 9:
        ip_address, date, method, path, protocol, status_code, file_size = parts[:7]
        if status_code.isdigit():
            status_code = int(status_code)
            file_size = int(file_size)
            total_size +=
