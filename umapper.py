#!/usr/bin/python
import sys
import re as regex

for line in sys.stdin:
    # remove all apsecial characters and white space
    line = regex.sub(r'^\W+|\W+$', '', line)
    words = regex.split(r'\W+', line)
    for word in words:
        print(word.lower() + '\t1')
