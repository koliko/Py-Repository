import Functions
import Other_files

#======================================#
# this part takes the user's name and  #
# greets the user                      #
#======================================#


greetings = "My name is Dzifa, What is your name? "
user_responds = input(greetings+" :")

print(Other_files.bots_template.format("Welcome " + user_responds))

while True:
    user_inputs = input(user_responds + " :")
    Functions.send_message(user_inputs)