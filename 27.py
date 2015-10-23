'''Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
Write it in three different ways:
1) using a for-loop,
2) using the higher order function map(), and 
3) using list comprehensions.'''

# already done

#2
l = ['apple', 'orange', 'cat']
print map( lambda x : len(x), l)

print map( len,  l)

#3
print [ len(i) for i in l]

