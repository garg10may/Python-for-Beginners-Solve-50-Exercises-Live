'''
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in,
but writing it yourself is nevertheless a good exercise.)
'''

a  = 'abd'

def length(x):
    c=0
    for _ in a:
        c = c +1 
    return c 

print length(a)