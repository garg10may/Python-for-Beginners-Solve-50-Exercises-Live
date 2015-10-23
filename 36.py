"""
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a
language, the works of an author, or in a single text. Define a function that given the file name of a text will return
all its hapaxes. Make sure your program ignores capitalization.
"""
import re

def hapax(x):
    d={}
    f = open(x)
    for word in re.findall('\w+', f.read().lower()):
        d[word] = d.get(word,0) + 1
    f.close()
    print [ k for k, v in d.items() if v==1]

hapax('36.txt')
        
        
        