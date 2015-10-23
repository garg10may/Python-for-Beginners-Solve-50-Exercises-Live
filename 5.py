# -*- coding: utf-8 -*-
'''
5.    Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). 
That is, double every consonant and place an occurrence of "o" in between. 
For example, translate("this is fun") should return the string "tothohisos isos fofunon".
'''

def translate(x):
    s = ''
    for i in x:
        if i not in ('aeiou'):
            s += i + "o" + i
        else:
            s += i 
    print s 
    
translate("this is fun")

    
    
    
    
