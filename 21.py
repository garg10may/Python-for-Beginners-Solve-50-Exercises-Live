'''
Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it.
Represent the frequency listing as a Python dictionary. 
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
'''


def char_freq(x):
    d ={}
    for i in x:
        d[i] = d.get(i,0) +1
    print d
    
    
char_freq("abbabcbdba.#$Fbdbdbabababcbcbab")


