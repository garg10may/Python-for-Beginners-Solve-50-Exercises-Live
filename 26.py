'''Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers
and returns the largest one. Then ask yourself: why define and call a new function, 
when I can just as well call the reduce() function directly? '''


def max_in_list(l):
    largest = reduce( lambda x,y: max(x,y) , l)
    return largest 
    
l = [1,2,3,78,34,90,36,9]

print max_in_list(l)


print reduce( max , l)

