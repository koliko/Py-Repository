"""this is a simple bots that talks with you.
   As time gose on the bots tries to learn from the user.
   Dzifa is just a small baby girl so don't make it cry.
"""
import random

#================================================#
# Defining the mind of Dzifa with dictonary      #
#================================================#

bots_mind = {

    "greetings":[],
    "greet_respond":[],
    "question":[],
    "responses":[],
    "memory":[]
}

#===================================================#
# Defining variables to be used in the bots design  #
#===================================================#

user_name = "{0}"
bots_output = "DZIFA : {0}"

#====================================================#
# Defing the function to be used in the bots design  #
#====================================================#

"""this part of the function deals with responds"""
def respond(message):

    if message in bots_mind:
        bots_output = random.choice(bots_mind["greetings"])
        user_input = input(user_name)
        if user_input in bots_mind["greet_respond"]:
            quest = (bots_output + bots_mind["question"])
            user_input = input(user_name)
            if user_input in random.choice(bots_mind["responses"]):
                print(quest)
    elif message not in bots_mind:
        print("I don't get you. I am still learning please teach me")
        print("are you ready to teach me?")
        user_input = input(" yes or no ?: ")
        if user_input == 'yes':
            print("thanks")
            bots_mind["memory"].append(user_input)
        else:
            print("I am cool with that")

"""this part of the function deals with sending message to the console"""

def send_message(message):
    pass


#=====================================================#
# Defing a loop that enable the bots to communicate   #
# with the user until the one the them sign's out     #
#=====================================================#
 
# TESTING

respond("how")