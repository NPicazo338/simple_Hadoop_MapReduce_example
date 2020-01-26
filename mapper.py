#!/usr/bin/env python
import sys
from sklearn.feature_extraction import stop_words

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace and lowercasing
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # creating set of stop words
    stopw = set(stop_words.ENGLISH_STOP_WORDS)

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stopw:
           print '%s\t%s' % (word, "1")
