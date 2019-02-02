#this is a simple bots that can answer simple questions
#we use dictonaries here. The quetions will be the keys and the responds will be the value.

import random
#=========================================#
# WELCOME TO CHITCHAT UNLIMITED           #
#=========================================#

name = "Grag"
weahter ="cloudy"
bots_template = "BOT: {0}"
user_template = "USER: {0}"

#defing a dictonary with the predefine responds.

responses = {"What is your name?": [
    "my name is {0}".format(name),
    "they call me {0}".format(name),
    "I go by {0}".format(name)],

             "What is today's weather?": [
                 "today's weather is {0}".format(weahter),
             "it's {0} today ".format(weahter)],
             "default": ["what are you saying?"]}

#defing the send message functions

def respond(message):
    #checking if the message is in the responds

    if message in responses:
        bots_template = random.choice(responses[message])

    else:
        bots_template = random.choice(responses["default"])

    return bots_template


def send_message(message):
    print(user_template.format(message))
    responds = respond(message)
    print(bots_template.format(responds))

user_input = input("User: ")

send_message(user_input)
