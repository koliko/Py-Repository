import journal

def main():
    print_header()
    run_event_loop()

def print_header():
    banner = "----------------------------------------------------"
    motd = "     PERSONAL JOURNAL APP"

    print(banner)
    print(motd)
    print(banner)

def run_event_loop():
    print("What do you want to do with your journal")

    #===================================================//
    # this part declares a list and add data to it     //
    #=================================================//

    journal_name = "defualt"
    journal_data = journal.load(journal_name)

    #=================================================//
    # this part performs check for the menu entry    //
    #===============================================//
    cmd = "Empty"

    while cmd != 'x' and cmd:
        cmd = input("L[l]ist entries, A[a]dd an entry, E[x]xit: ")
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd == "x":
            print("E")
        elif cmd != 'x' and cmd:
            print("Sorry we don\'t understand '{}'".format(cmd))
    print("Done, goodbye")
    journal.save(journal_name,journal_data)

def add_entries(data):
    text = input("Type your entries: ")
    journal.add_entries(text, data)

def list_entries(data):
    print("your journal entries")
    myentries = reversed(data)
    for idx,entries in enumerate(myentries):
        print("[{}] {}".format(idx +1, entries))

if __name__ == '__main__':
    main()