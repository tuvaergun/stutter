#!/usr/bin/python

import sys
import itertools

seed = sys.argv[1]

with open('chars.txt', 'r') as f:
    data = f.read().split('\n')

newlist = []

for letter in seed:
    for line in data:
        if letter in line:
            newlist.append(line)

words = map(''.join, itertools.product(*((list(c)) for c in newlist)))

for word in words:
    print word

print "Seed '%s' generated %s words" % (seed, len(words))