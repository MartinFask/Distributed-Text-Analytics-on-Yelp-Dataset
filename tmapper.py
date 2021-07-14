#!/usr/bin/python
import sys
import re as regex


for line in sys.stdin:
    # remove all apsecial characters and white space
    line = regex.sub(r'^\W+|\W+$', '', line)
    words = regex.split(r'\W+', line)
    # create the trigram using zip
    trigram = zip(*[words[i:] for i in range(3)])
    for j in trigram:
        print(' '.join(j).lower() + '\t1')
