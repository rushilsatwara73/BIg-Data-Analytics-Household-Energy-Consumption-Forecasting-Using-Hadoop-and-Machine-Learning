#!/usr/bin/env python3
import sys

current_key = None
total = 0.0
count = 0

def emit(key, total, count):
    if key is not None and count > 0:
        print(f"{key}\t{total/count:.4f}\t{count}")

for line in sys.stdin:
    parts = line.rstrip("\n").split("\t")

    if len(parts) != 2:
        continue

    key, value = parts

    try:
        value = float(value)
    except ValueError:
        continue

    if key != current_key:
        emit(current_key, total, count)
        current_key = key
        total = 0.0
        count = 0

    total += value
    count += 1

emit(current_key, total, count)
