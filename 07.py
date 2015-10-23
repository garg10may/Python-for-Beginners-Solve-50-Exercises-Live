'''
Define a function reverse() that computes the reversal of a string. 
For example, reverse("I am testing")
should return the string "gnitset ma I".
'''

def reverse(x):
    new =[]
    for i in range(len(x))[::-1]:
        new.append(x[i])
    print ''.join(new)

reverse('I am testing')