#!/usr/bin/python
import sys

previous = None
temp = {}
days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
for line in sys.stdin:
    # skip empty lines
    if not line.strip():
        continue
    key, day, value = [x.strip() for x  in line.split(',')]
    # if this is the first time we see this key, print results of the previous key
    if key != previous:
        if temp:
            # print in a general format (Mon,  Tue, Wed, Thu, Fri, Sat, Sun)
            for day in days:
                num_of_checkins = 0
                if day in temp:
                    num_of_checkins = temp[day]
                print("{}, {}, {}".format(key, day.capitalize(), num_of_checkins))
        # store the data for the new key
        temp = {}
    if day not in temp:
        # to take into consideration both lower/uppr cases
        d = day.lower()
        temp[d] = 0
        temp[d] += int(value)
    previous = key
