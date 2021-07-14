#!/usr/bin/python
import sys

count = 1

for line in sys.stdin:
    # skip the first line
    if count == 1:
        count += 1
        continue
    get_data = [x.strip() for x in line.split(',')]
    # print the business_id, days and checkins
    print("{}, {}, {}\n".format(get_data[0],get_data[1],get_data[3]))
