# this is a bots that repeate what you have said.

bot_template = "Bot: {0}"
user_responds = "user {0}"

#this function responds to user interface

def respond(message):
    bot_message = "I can here you. You said: " + message
    return bot_message

#this function sends messages to the bot

def send_message(message):
    print (user_responds.format(message))
    responds = respond(message)

    #print the bots template including the bots responds
    print(bot_template.format(responds))


send_message("What is today")