'''
The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers,
respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are?
Write a function max_in_list() that takes a list of numbers and returns the largest one.
'''

def max1(l):
    max =0
    for i in range(len(l)-1):
        if l[i] > l[i+1] and l[i]>max:
            max = l[i]
        elif l[i+1]>max:
            max = l[i+1]
    print max
    

max1([1,2,34,4,6,345])