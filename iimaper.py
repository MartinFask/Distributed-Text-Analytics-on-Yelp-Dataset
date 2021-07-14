#!/usr/bin/python


import sys
import csv


for line in csv.reader(sys.stdin):
    # keep the business_id column
    bid = line[0]
    # keep the cateroies column
    cat = line[12].split(';')
    for i in cat:
        print("{}: {}\n".format(i, bid))
