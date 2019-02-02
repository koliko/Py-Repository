import time
import datetime
#===========================================//
# working with functions for the app       //
#=========================================//


def print_header():

    banner = "-----------------------------------------------"
    motd = "          BIRTHDAY APP"

    print(banner)
    print(motd)
    print(banner)
    print()

def get_birthday_from_user():
    print("Tell us when you were born: ")
    year = int(input("Year [YYYY]: "))
    day = int(input("Day [DD]: "))
    month = int(input("Month [MM]: "))

    birthday = datetime.datetime(year,month,day)

    return birthday

def compute_days_between_dates(original_date,now):
    dt = datetime.timedelta

    date1 = now
    date2 = datetime.datetime(now.year,original_date.month,original_date.day )

    dt = date1 - date2
    day = int(dt.total_seconds() /60 /60 /24)
    return day

def print_birthday_information(days):
    if days < 0:
        print("Your birthday is in {} days!".format(-days))
    elif days > 0:
        print(" You had your birthday already this year! {} days ago".format(days))
    else:
        print("Happy birthday")

def main():

    b = print_header()

    body = get_birthday_from_user()

    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(body,now)
    print_birthday_information(number_of_days)

def menu():

    in_out = input("[Login = yes], [Exit = no]: ")

    goTo = 'yes'
    noTo = 'no'

    while in_out==goTo:

        menu_input = input("Do you want to check your birthday?: ")

        goTo = 'yes'
        if(menu_input == goTo):
           main()
        else:
          exit()
menu()