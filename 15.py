'''Write a function find_longest_word() that takes a list of words and returns the length of the longest one.'''

def maps(x):
    k=[]
    for i in x:
        k.append(len(i))
    print max(k)
    
        
maps(['apple','orange','cat'])