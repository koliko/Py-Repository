import random



print('--------------------------------------------')
print('       GUESS THAT NUMBER GAME               ')
print('--------------------------------------------')
print()


the_number = random.randint(0, 100)
guss = -1

while guss != the_number:

    guss_text = input("Gusss a number  between 0 and 100: ")

    guss = int(guss_text)

    if(guss < the_number):
        print("You guss of %s was too low" %guss)

    elif(guss > the_number):

        print("You guss of %s is too high" %guss)


    else:
        print('========================================================')
        print("You guss %s that the lucky number you WIN !!!!!" %guss)
        print('========================================================')
print("Done")

