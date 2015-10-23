'''
A sentence splitter is a program capable of splitting a text into sentences. 
The standard set of heuristics for sentence splitting includes (but isn't limited to) the following rules:
Sentence boundaries occur at one of "." (periods), "?" or "!", except that
1. Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
2. Periods followed by a digit with no intervening whitespace are not sentence boundaries.
3. Periods followed by whitespace and then an upper case letter, but preceded by any of a short list  of titles are not sentence boundaries. 
   Sample titles include Mr., Mrs., Dr., and so on.
4  Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries
   (for example, www.aptex.com, or e.g).
5. Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.

Your task here is to write a program that given the name of a text file is able to write its content with each sentence on a separate line.
Test your program with the following short text:

Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? 
Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. 

The result should be:

Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind?
Adam Jones Jr. thinks he didn't.
In any case, this isn't true...
Well, with a probability of .9 it isn't.
'''

import re 

text = "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. \
Did he mind? Adam Jones Jr. thinks he didn't. In any case, \
this isn't true... Well, with a probability of .9 it isn't."

# Method 1
for i in re.findall(r'[A-Z][a-z]+\.?.*?[.?!](?= [A-Z]|$)', text):
    print i

print '*'*80

#Method 2 - using verbose mode. 
for i in re.findall(r'''
						[A-Z][a-z]+\.?   # Starts with Capital includes (Mr., Mrs.)
                        .*?              # followed by anything
                        [.?!]            # ends with a (.)(?)(!)
                        (?=\s[A-Z]|$)    # is followed by whitespace and a capital letter
                     ''', text, re.X):
    print i

print '*'*80 

#Method 3
for i in re.split(r'(?<=[^Mr|Mrs|Dr][.?!])\s(?=[A-Z])', text):
    print i


