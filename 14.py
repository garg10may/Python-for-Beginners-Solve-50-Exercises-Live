'''Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.'''


def maps(x):
    k=[]
    for i in x:
        k.append(len(i))
    print k
    
    
maps(['apple','orange','cat'])

l = ['apple','orange','cat']

print map( len, l)
