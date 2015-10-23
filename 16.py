'''Write a function filter_long_words() that takes a list of words
 and an integer n and returns the list of words that are longer than n.'''
 
def filter_long_words(x,n):
    k=[]
    for i in x:
        if len(i)>n:
            k.append(i)
    print k
    
    
filter_long_words(['apple','orange','cat'], 4)