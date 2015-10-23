'''
Represent a small bilingual lexicon as a Python dictionary in the following fashion
 {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"} 
 and use it to translate your Christmas cards from English into Swedish. Use the higher order function map()
  to write a function translate() that takes a list of English words and returns a list of Swedish words.
'''

def translate(x):
    d ={"merry":"god", 
        "christmas":"jul",
        "and":"och", 
        "happy":"gott",
        "new":"nytt",
        "year":"ar"}
    l = x.split()
    print map ( lambda x: d[x], l)
    

translate("merry new christmas and happy new year")
