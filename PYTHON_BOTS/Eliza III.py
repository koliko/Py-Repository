import re
import random

#defing a dictonary name rule

rules = {'if (.*)':
             ["Do you really think it's likely that {0}", 'Do you wish that {0}', 'What do you think about {0}',
              'Really--if {0}'],
         'I want (.*)':
             ['What would it mean if you got {0}', 'Why do you want {0}', "What's stopping you from getting {0}"],
         'do you think (.*)':
             ['if {0}? Absolutely.', 'No chance'],
         'do you remember (.*)':
             ['Did you think I would forget {0}', "Why haven't you been able to forget {0}", 'What about {0}', 'Yes .. and?']
         }

def match_rules(rules,message):
    response, phrase = "default",None

    for pattern, responses in rules.items():

        #=========================================#
        # this part creates a matching sequence   #
        #=========================================#

        match = re.search(pattern,message)

        if match is not None:
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
        return  response,phrase


def replace_pronouns(message):
    message = message.lower()

    if 'me' in message:
        return re.sub('me',"you",message)
    if 'my' in message:
        return re.sub('my',"your",message)
    if 'you' in message:
        return re.sub('you',"me",message)
    if "your" in message:
        return re.sub('your',"my",message)
    return message

print(replace_pronouns("my last birthday"))
print(replace_pronouns("when you went to Florida"))
print(replace_pronouns("I had my own castle"))