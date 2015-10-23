'''
Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, 
you should (also) write it using two nested for-loops.
'''

def overlapping(m,n):
    l1 =len(m)
    l2 = len(n)    
    for i in range(l1):
        for j in range(l2):
            if m[i]==n[j]:
                status =1
                break
        else:
            status =0
    if status ==1:
        print True
    else:
        print False
         
    
overlapping(['a','e'], ['c','d'])