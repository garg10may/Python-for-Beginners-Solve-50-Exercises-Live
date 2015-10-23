'''
Define a function is_palindrome() that recognizes palindromes
(i.e. words that look the same written backwards). For example,
is_palindrome("radar") should return True.
'''
  
def is_palindrome(x):
    if x == x[::-1]:
        print True
    else:
        print False
        
is_palindrome("aradar")