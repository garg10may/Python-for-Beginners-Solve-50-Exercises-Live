'''
4.    Write a function that takes a character
 (i.e. a string of length 1) and returns True if 
 it is a vowel, False otherwise.
'''

def vowel(x):
    if x in ('aeiou'):
        return True
    else:
        return False
    
    
print vowel('b')