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

# Grid contains the previous lines
grid = []

for i in xrange(10):
    # Genetaring operator values:
    offset = random.randrange(len(alphabet))
    # Computing the new line given the operators:
    line = new_line(offset=offset)

    # Search for words:
    for char_position in xrange(len(line)):
        char = line[char_position]

        for start_position in xrange(char_position):
            word = line[start_position:char_position+1]
            #print 'word=', word
            if word in words:
                print 'MATCH', word

    # Printing line
    print line, 'o%02i' % offset
    # Saving line to the grid:
    grid.append(line)