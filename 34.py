'''Write a procedure char_freq_table() that, when run in a terminal, accepts a file name
 from the user, builds a frequency listing of the characters contained in the file, and
 prints a sorted and nicely formatted character frequency  table to the screen.'''
 
 
example = __import__('21')

def char_freq_table():
    n = raw_input('Please enter a file name: ')
    example.char_freq(open(n).read())
    
    
char_freq_table()
