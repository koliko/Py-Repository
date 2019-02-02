import re
import random

#=========================================#
# defining the function to handle the chat#
#=========================================#

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

#================================================#
# define the variables to be used in the program #
#================================================#

bots_templete = 'ELIZA : {0} '
user_templete = 'USER : {0}'

#================================================#
# this parts contain functions that performs     #
# particular activities in the program           #
#================================================#

'''the first fucntion is the match rule function
    this function search and match conversation
    it takes to agreements [ rules and message 
'''
def match_rule(rules, message):
    response, phrase = "default", None

    '''iteration over the rules'''

    for pattern, responeses in rules.items():
        '''matching the strings '''

        match = re.search(pattern, message)
        '''checking if there is a match'''

        if match is not None:
            response = random.choice(responeses)
        if '{0}' in response:
            phrase = match.group(1)
        return response,phrase

'''this second function is for the replacment 
    of pronounes
'''
def replace_pronouns(message):
    '''convert any string to lower case'''

    message = message.lower()

    if 'me' in message:
        return re.sub('me','you',message)
    if 'my' in message:
        return re.sub('my','your',message)
    if 'your' in message:
        return re.sub('your','my',message)
    if 'you' in message:
        return re.sub('you','me',message)
    return message

'''this third function is for the responds 
    item. for the bots to respond we use 
    this function
'''
def respond(message):
    response,phrase = match_rule(rules,message)

    if '{0}' in response:
        phrase = replace_pronouns(phrase)
        response = response.format(phrase)

    return response

'''this fourth function takes care of the 
    send message to the console
'''

def send_message(message):
    print(user_templete.format(message))
    responds = respond(message)
    print(bots_templete.format(responds))
#
# while True:
#
# #     user_input = input(" USER :")
#     send_message(user_input)
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")