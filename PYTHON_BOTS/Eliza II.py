
import re
import random

#defing a dictonary name rule

rules = {'if (.*)':
             ["Do you really think it's likely that {0}", 'Do you wish that {0}', 'What do you think about {0}', 'Really--if {0}'],
         'I want (.*)':
    ['What would it mean if you got {0}', 'Why do you want {0}', "What's stopping you from getting {0}"],
         'do you think (.*)':
             ['if {0}? Absolutely.', 'No chance'],
         'do you remember (.*)':
    ['Did you think I would forget {0}', "Why haven't you been able to forget {0}", 'What about {0}', 'Yes .. and?']
         }

#define match_rule

def match_rule(rules, message):
    response, phrase = "default", None

    #iterate over the rules dictionary

    for pattern, responses in rules.items():

    #creating a match object
     match = re.search(pattern,message)
    if match is not None:
        response = random.choice(responses)
        if '{0}' in response:
            phrase = match.group(1)
    return response, phrase

print(match_rule(rules, "do you remember your last birthday"))
