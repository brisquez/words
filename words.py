'''
    Experimental research on words and poetry based on interactively generated
    alphabet grids.
'''

import random

import string
alphabet = string.lowercase

words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

def new_line(offset=0):
    line = alphabet
    line = line[offset:] + line[:offset]
    return line

for i in xrange(10):
    offset = random.randrange(len(alphabet))
    print new_line(offset=offset), 'o%02i' % offset