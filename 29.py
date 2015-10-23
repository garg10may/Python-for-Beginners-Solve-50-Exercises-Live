'''
Using the higher order function filter(), define a function filter_long_words() 
that takes a list of words and an integer n and returns the list of words that are longer than n
'''

n=2
x = ['abc','b','adfadfasd']
print filter(lambda x: len(x)>n, x)


