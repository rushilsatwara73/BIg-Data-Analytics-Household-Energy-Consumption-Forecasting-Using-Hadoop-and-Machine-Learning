#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.rstrip("\n")
    parts = line.split("\t", 1)

    if len(parts) == 2:
        key, value = parts
        try:
            print(f"{key}\t{float(value)}")
        except ValueError:
            continue
