'''
A pangram is a sentence that contains all the letters of the English alphabet at least once, for example:
The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence
to see if it is a pangram or not.
'''

import string

def pangram(x):
    for i in string.letters[:26]:
        if i in x.lower():
            status =1
        else:
            print 'not a pangram'
            status =0
            break
        
    if status==1:
        print 'pangram'  
        
pangram('The q brown fox jumps over the lazy dog')

