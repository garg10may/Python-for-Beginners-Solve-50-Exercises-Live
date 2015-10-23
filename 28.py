'''
Write a function find_longest_word() that takes a list of words and returns the length of the longest one. 
Use only higher order functions.
'''


l = ['apple', 'orange', 'cat']
print max(map( len,  l))