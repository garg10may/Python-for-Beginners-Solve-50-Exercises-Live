'''An alternate is a word in which its letters, taken alternatively in a strict
 sequence, and used in the same order as the original word,
  make up at least two other words. All letters must be used, 
  but the smaller words are not necessarily of the same length. 
  For example, a word with seven letters where every second letter 
  is used will produce a four-letter word and a three-letter word. 
  Here are two examples:
      "board": makes "bad" and "or".
      "waists": makes "wit" and "ass".
Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, 
write a program that goes through each word in the list
 and tries to make two smaller words using every second letter.
  The smaller words must also be members of the list. 
  Print the words to the screen in the above fashion.
'''
import urllib2
import time

data = urllib2.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt').read()
words_list = set(data.split('\n'))

start = time.clock()
for line in words_list:
    total =[]
    alternate, alternate2 = '',''
    for i in range(0,len(line),2):
        alternate = alternate + line[i]
    if alternate in words_list and len(alternate)>2:
        total.append(alternate)        
    for i in range(1,len(line),2):
        alternate2 = alternate + line[i]
    if alternate2 in words_list and len(alternate2)>2:
        total.append(alternate2)
    if len(total)==2:
        print "%s: makes %s and %s" %(line,alternate, alternate2)
end = time.clock()
print end-start