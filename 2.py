'''
Define a function max_of_three() that takes three numbers as
 arguments and returns the largest of them.
'''

def max_of_three(a,b,c):
    if a>b and a>c:
        print a 
    elif b>c:
        print b 
    else:
        print c 
        
print max_of_three(0,15,2)