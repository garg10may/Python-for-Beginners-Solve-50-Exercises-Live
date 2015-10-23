'''
Write a program that will calculate the average word length of a text stored in a file 
(i.e the sum of all the lengths of the word tokens in the text, divided by the number
 of word tokens).
'''
import re

def avg_length(x):
    count = 0.0
    f = open(x)
    words = re.findall('\w+', f.read())
    for word in words:
        count += len(word)
    return count/len(words)

print avg_length('38.txt')