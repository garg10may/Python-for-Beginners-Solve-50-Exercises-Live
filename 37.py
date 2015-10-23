'''
Write a program that given a text file will create a new text file in which all the lines
from the original file are numbered from 1 to n 
(where n is the number of lines in the file).
'''

f = open('37.txt')

f_out = open('37_out.txt', 'w')

count =1
for i in f:
    print i
    f_out.write(str(count) + '. ' + i)
    count +=1
    
f.close()
f_out.close()

