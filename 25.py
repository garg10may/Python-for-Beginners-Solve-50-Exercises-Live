'''
In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going.
A simple set of heuristic rules can be given as follows:
If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant, double the final letter before adding ing
By default just add ing
Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
returns its present participle form.
Test your function with words such as lie, see, move and hug. 
However, you must not expect such simple rules to work for all cases.
'''

def make_ing_form(x):
    if x.endswith('e')  and not x.endswith('ie') and not x.endswith('ee') and not len(x)==2:
        x = x[:-1] + 'ing'
    elif x.endswith('ie'):
        x = x[:-2] + 'ying'
    elif len(x)==3 and x[-2] in ('aeiou') and x[-1] not in ('aeiou') and x[-3] not in ('aeiou'):
        x += x[-1] + 'ing'
    else:
        x += 'ing'
    print x
make_ing_form('flee')
        