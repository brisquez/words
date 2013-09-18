'''
    Experimental research on words and poetry based on interactively generated
    alphabet grids.
'''

import string
alphabet = string.lowercase

words = [word.strip() for word in open('/usr/share/dict/words').readlines()]
