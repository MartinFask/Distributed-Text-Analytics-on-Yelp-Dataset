#!/usr/bin/python
import sys

previous = None
sum = 0

for line in sys.stdin:
    key, value = line.split('\t')
    # if this is the first time we see this key
    if key != previous:
        if previous is not None:
            # if we reach the edge of same keys, then print the previous key and their sum
            print(str(sum) + '\t' + previous)
        previous = key
        sum = 0
    sum = sum + int(value)


print(str(sum) + '\t' + previous)
