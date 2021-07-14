#!/usr/bin/python
import sys

previous = None
temp = []

for line in sys.stdin:
    # skip empty lines
    if not line.strip():
        continue
    category, business_id = [x.strip() for x  in line.split(':')]
    # if this is the first time we see this category
    if category != previous:
        if previous != None:
            print("{}: {}".format(previous, ', '.join(temp)))
        temp = []
    temp.append(business_id)
    previous = category
