'''
In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this 
word by guessing, and in return receive two kinds of clues: 
    1) the characters that are fully correct,  with respect to identity as well as to position, and
    2) the characters that are indeed present in the word, but which are placed in the wrong position.
Write a program with which one can play Lingo. Use square brackets to mark characters correct in the sense of 
    1), and ordinary parentheses to mark characters correct in the sense of
    2). Assuming, for example, that the program conceals the word "tiger", 
you should be able to interact with it in the following way:

>>> import lingo
snake
Clue: snak(e)
fiest
Clue: f[i](e)s(t)
times
Clue: [t][i]m[e]s
tiger
Clue: [t][i][g][e][r]
'''


def lingo(x):
    n = raw_input('Please input your five letter guess!\n')
    
    while n != x:
        output =''
        for index, i in enumerate(n):
            if i in x:
                if n[index]==x[index]:
                    output += '[' + i + ']'
                else:
                    output += '(' + i + ')'
            else:
                output += i 
        print 'Clue:' + output  
        n = raw_input('Please input your five letter guess!\n') 
    print 'Success'    
            
lingo('snake')

    