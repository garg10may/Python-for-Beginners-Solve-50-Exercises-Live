'''An anagram is a type of word play, the result of rearranging 
the letters of a word or phrase to produce a new word or phrase,
 using all the original letters exactly once; e.g., orchestra = carthorse. 
 Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, 
 write a program that finds the sets of words that share the same characters
 that contain the most words in them.'''

import urllib
import time


def anagram():
    start = time.clock()
    
    f = urllib.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt')
    words = set(f.read().split('\n'))    
    d = { ''.join(sorted(i)):[] for i in words}
    
    for i in words:
        d[''.join(sorted(i))].append(i)    
    max_len = max( len(v) for v in d.values())    
    
    for v in d.values():
        if len(v)==max_len:
            print v 
            
    end = time.clock()
    print end - start 
    

anagram()