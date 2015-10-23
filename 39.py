# -*- coding:utf-8 -*-
'''
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20.
(Source: http://inventwithpython.com) This is how it should work when run in a terminal:
>>> import guess_number
Hello! What is your name?
Torbj�rn
Well, Torbj�rn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbj�rn! You guessed my number in 3 guesses!
'''
import random

def check():
    global count  # good example of use of global
    guess = int(raw_input("Take a guess\n"))
    if guess == no:
        print "Good job, %s! You guessed my number in %d guesses!" %(name,count)
    if guess < no:
        print "Your guess is too low."
        count +=1        
        check()          
    if guess > no:
        print "Your guess is too high"
        count +=1
        check()

name = raw_input("Hello! What is your name?\n")
print "Well, " + name + ", I am thinking of a number between 1 and 20"
no = random.randint(1,20)
print no
global count
count  =1
check()

'''
import random

name = raw_input("Hello! What is your name?\n")
print "Well, " + name + ", I am thinking of a number between 1 and 20"
no = random.randint(1,20)
guess = int(raw_input("Take a guess\n"))
count =1

while guess != no:    
    if guess < no:
        print "Your guess is too low."                 
    if guess > no:
        print "Your guess is too high"
    count +=1
    guess = int(raw_input("Take a guess\n"))

print "Good job, %s! You guessed my number in %d guesses!" % (name ,count)

'''