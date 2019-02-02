#this is just the first part of eliza that ask
#questions and respons base on users answer.

import random

#definiing variables to be used

user_template = "USER : {0}"
bots_template = "ELIZA: {0}"

#definining questions, statments and answers

responses = {"statement":
                 ["tell me more","why do you think that?","how long have you felt this way?",
                  "I find that extramely intresting","can you back that up?", "oh wow?",":)"],
             "question": ["I don't know ", ":(","you tell me !"]
             }
    #define the respond function

def respond(message):
    #checking if message is in responds
    if message.endswith("?"):
        return random.choice(responses["question"])
    return random.choice(responses["statement"])

#defing a function that send the message

def send_message(message):
    print(user_template.format(message))
    responds = respond(message)
    print(bots_template.format(responds))
user_input = input("User: ")
send_message(user_input)