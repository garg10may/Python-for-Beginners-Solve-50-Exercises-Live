'''Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
and use it to translate your Christmas cards from English into Swedish.
That is, write a function translate() that takes a list of English words and returns a list of Swedish words.'''

def tanslate(x):
    new=[]
    d = {"merry":"god",
          "christmas":"jul", 
          "and":"och", 
          "happy":"gott", 
          "new":"nytt", 
          "year":"ar"}
    l = x.split(' ')
    for i in l:
        new.append(d[i])
    print new 
    print ' '.join(new)         
        
tanslate('merry christmas and happy new year')
