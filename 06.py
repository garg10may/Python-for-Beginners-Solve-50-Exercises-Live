'''
Define a function sum() and a function multiply() that sums and multiplies 
(respectively)  all the numbers in a list of numbers. For example, sum([1, 2, 3, 4])
 should return 10,   and multiply([1, 2, 3, 4]) should return 24.
'''


def sum1(x):
    c=0
    for i in x:
        c += i 
    return c

print sum1([1, 2, 3, 4])

def multiply(x):
    c=1
    for i in x:
        c *= i 
    return c

print multiply([1, 2, 3, 4])
