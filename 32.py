
'''Write a version of a palindrome recogniser that accepts a 
file name from the user, reads each line, and prints the line to the screen
 if it is a palindrome.'''
 

def palindrome1(x):
    for i in open(x).read().split('\n'):
        if i==i[::-1]:
            print i + " is palindrome"
            
            
palindrome1('32.txt')


def palindrome2(x):
    for i in open(x).readlines():
        i = i.rstrip()
        if i==i[::-1]:
            print i + " is palindrome"
            
palindrome2('32.txt')
            