import re
import random
import Other_files
import Main_Mind

#=============================================#
# This function is for matching strings or    #
# sentence. This function only match and retu-#
# rn items.                                   #
#=============================================#

def match_rules(rules, message):
    response, phrase = "i have no Idea", None

    if response is 'i have no Idea':
        say_something = input("i have no Idea, will you teach me? :")

        if say_something == 'yes':
            print('there comes the good teacher')
            response = 'teach me'

    '''iterating through the mind'''

    for pattern , responeses in rules.items():
        match = re.search(pattern,message)

        '''checking if there is a match'''

        if match is not None:

            response = random.choice(responeses)

        if '{0}' in response:
             phrase = match.group(1)
        return response, phrase

#================================================#
# this function is for replacing pronouns        #
#================================================#


def replace_pronouns(message):
    '''convert every string to a lower case'''

    message = message.lower()

    if Main_Mind.part_of_speech in message:
        return re.sub(Main_Mind.part_of_speech('noun'),Main_Mind.part_of_speech('pronoun'),message)

    for noun in Main_Mind.part_of_speech('noun'):
        pronoun = random.choice(Main_Mind.part_of_speech('pronoun'))
        return re.sub(pronoun,noun,message)
    return message

#===================================================#
# this function is for the respond by the bots and  #
# the user                                          #
#===================================================#

def respond(message):
    responses, phrase = match_rules(Main_Mind.rules,message)

    if '{0}' in responses:
        phrase = replace_pronouns(Other_files.user_template)
        responses = responses.format(phrase)
    return responses

#=====================================================#
# this function is for the sending of message to the  #
# console                                             #
#=====================================================#

def send_message(message):
    # print(Other_files.user_template.format(message))
    response = respond(message)
    print(Other_files.bots_template.format(response))