
'''
Implement the higher order functions map(), filter() and reduce().
(They are built-in but writing them yourself may be a good exercise.)
'''

def map1(f, l):
    new=[]
    for i in l:
        new.append(f(i))
    return new
        
    
def filter1(f, l):
    new =[]
    for i in l:
        if f(i) == True:
            new.append(i)
    return new
        
def reduce1(f, l):
    new = l[0]
    for i in l[1:]:
        new = f(new, i)
    return new

print reduce1(max, [1,2,-45,3,0])
        


    
    
