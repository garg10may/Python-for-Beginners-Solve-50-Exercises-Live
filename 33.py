'''
According to Wikipedia, a semordnilap is a word or phrase that spells a different 
word or phrase backwards. ("Semordnilap" is itself "palindromes" spelled backwards.)
Write a semordnilap recogniser that accepts a file name (pointing to a list of words)
from the user and finds and prints all pairs of words that are semordnilaps to the screen.
For example, if "stressed" and "desserts" is part of the word list, the the output
should include the pair "stressed desserts". Note, by the way, that each pair by itself 
forms a palindrome!
'''

def semordnilap(x):
    f = open(x).read()
    words = f.split('\n') 
    while words:
        a = words[0]
        words.remove(a)
        if a[::-1] in words:
            print a + ' and ' + a[::-1] + ' are semordnilap'
                
semordnilap('33.txt')