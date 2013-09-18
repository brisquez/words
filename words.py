'''
    Experimental research on words and poetry based on interactively generated
    alphabet grids.
'''

import random

import string
alphabet = string.lowercase

words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

def new_line(offset=0, reverse=False):
    line = alphabet
    if offset:
        line = line[offset:] + line[:offset]
    if reverse:
        line = ''.join(list(reversed(line)))
    return line

# Grid contains the previous lines
grid = []
# Matches coordinates, per line:
matches = []

for i in xrange(10):
    line_matches = []

    # Genetaring operator values:
    offset = random.randrange(len(alphabet))
    reverse = random.randrange(2) > 0
    # Computing the new line given the operators:
    line = new_line(offset=offset, reverse=reverse)

    print line, 'o%02i' % offset, 'r%01i' % reverse

    # Search for words:
    for char_position in xrange(len(line)):
        char = line[char_position]

        # Searching horizontally words ending in current char:
        for start_position in xrange(char_position):
            word = line[start_position:char_position+1]
            #print 'word=', word
            if word in words:
                line_matches.append(('h', char_position, word))
                print 'MATCH', word

        # Searching vertically words ending in current char:
        # (Maximum 10 letters long)
        vertical_line = ''.join(prev[char_position] for prev in grid[-10:]) \
                      + char
        #print 'VL', vertical_line
        for start_position in xrange(len(vertical_line)): 
            word = vertical_line[start_position:]
            if len(word) > 1:
                #print 'v_word=', word
                if word in words:
                    line_matches.append(('v', char_position, word))
                    print 'V_MATCH', word

    # Printing line
    #print line, 'o%02i' % offset
    # Saving line to the grid:
    grid.append(line)
    matches.append(line_matches)

for line in grid:
    print line

print matches