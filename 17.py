'''Write a version of a palindrome recognizer that also accepts phrase palindromes such as 
"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
"Rise to vote sir", or the exclamation "Dammit, I'm mad!". 
Note that punctuation, capitalization, and spacing are usually ignored.'''


def palindrome(x):
    l=[]
    for i in x:
        if i.isalpha():
            l.append(i.lower())
    print ''.join(l)
    if l==l[::-1]:
        print 'palindrome'
    else:
        print 'Not a palindrome'       

palindrome("Go hang a salami I'm a lasagna hog.")