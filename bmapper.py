#!/usr/bin/python
import sys
import re as regex


for line in sys.stdin:
    # remove all apsecial characters and white space
    line = regex.sub(r'^\W+|\W+$', '', line)
    words = regex.split(r'\W+', line)
    # create the bigram using zip
    bigram = zip(*[words[i:] for i in range(2)])
    for j in bigram:
        print(' '.join(j).lower() + '\t1')
