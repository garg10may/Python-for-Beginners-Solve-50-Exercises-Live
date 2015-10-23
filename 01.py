'''
Define a function max() that takes two numbers as arguments and returns
the largest of them. Use the if-then-else construct available in Python.
(It is true that Python has the max() function built in, but writing it
yourself is nevertheless a good exercise.)
'''

def max1(m,n):
    if m>n:
        return m 
    else:
        return n 

print max1(6,5)
