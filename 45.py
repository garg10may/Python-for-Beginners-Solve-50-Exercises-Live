'''
A certain childrens game involves starting with a word in a particular category. Each participant in
 turn says a word, but that word must begin with the final letter of the previous word. 
 Once a word has been given, it cannot be repeated. If an opponent cannot give a word in the category, 
 they fall out of the game. For example, with "animals" as the category,

Child 1: dog 
Child 2: goldfish
Child 1: hippopotamus
Child 2: snake
...
Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names 
(extracted from Wikipedia's list of Pokemon) and generate the/a sequence with the highest possible
 number of Pokemon names where the subsequent name starts with the final letter of the preceding name.
  No Pokemon name is to be repeated.'''
from collections import defaultdict
import time


pokemon = '''audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'''.split()

def find(chain):
    last_character = chain[-1][-1]
    options = d[last_character] - set(chain)
    
    if not options:
        return chain
    else:
        return max( (find(chain+[i]) for i in options), key=len)            
    
 
start = time.clock()   

d = defaultdict(set)       
for word in pokemon:
    d[word[0]].add(word)

print max( (find([word]) for word in pokemon), key=len)

end = time.clock()
print end - start

#try bottom down approach
def find2(chain):
    first_character = chain[0][0]
    options = d[first_character] -set(chain)
    
    if not options:
        return chain
    else:
        return max( (find2([i]+ chain) for i in options), key=len)
    
start = time.clock()
d = defaultdict(set)
for word in pokemon:
    d[word[-1]].add(word)
      
print max( (find2([word]) for word in pokemon), key=len)
end = time.clock()
print end - start 

'''
def find(chain):
    l=[]
    last_character = chain[-1][-1]
    options = d[last_character] - set(chain)
    
    if not options:
        return chain
    else:
        for i in options:
            l.append(find(chain+[i]))
        return max(l, key=len)
            
        #return [ find(chain+[i]) for i in options]        
        
pokemon = set(pokemon)

d = defaultdict(set)       
for word in pokemon:
    d[word[0]].add(word)

print max( [find([word]) for word in pokemon], key=len)


def find(chain):
    last_character = chain[-1][-1]
    options = d[last_character] - set(chain)
    
    if not options:
        return chain
    else:
        for i in options:
            find(chain+[i])
    #to understand importance of return, here once we are in else block nothing is returned       
    
    
pokemon = set(pokemon)

d = defaultdict(set)       
for word in pokemon:
    d[word[0]].add(word)

print [find([word]) for word in pokemon]
'''




