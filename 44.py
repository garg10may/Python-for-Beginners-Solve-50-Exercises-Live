'''
Your task in this exercise is as follows:

Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it consists entirely of pairs
of opening/closing brackets (in that order), none of which mis-nest.
Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK
'''

import random

def find_balanced(n):
    count_left, count_right = 0,0
    s = [random.choice(['[',']']) for i in range(int(n))]
    for i in s:
        if count_left == count_right:
            if i ==']':
                return ''.join(s) + ' not balanced'
        if i =='[':
            count_left +=1
        else:
            count_right +=1
    if count_left == count_right:
        return ''.join(s) + '  balanced'
    else:
        return ''.join(s) + ' not balanced'
        
for i in range(20):
    print find_balanced(50)

