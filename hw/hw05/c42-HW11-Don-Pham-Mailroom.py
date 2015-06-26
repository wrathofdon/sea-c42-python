# Dictionary sorting guide: http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
# Reverse order: http://stackoverflow.com/questions/5455606/how-to-reverse-order-of-keys-in-python-dict


contacts = {}


def statup_boot():
    print("Welcome to Mailroom Madness")
    print("Choose from the following:")
    print("T - Send a (T)hank You and Print E-Mail")
    print("R - Create a (R)eport")
    response = input("quit - Quit the program")
    response = response[:1]
    response = response.lower()
    if (response == "q"):
        break
    elif (response == "t"):
        thank_you()
    elif (response == "r"):
        generate_report()
    else:
        print("Invalid entry.")
        startup_boot()


def thank_you():
    print("Please enter a name, or choose from the following:")
    print("list - Print a list of previous donors")
    donor = input("quit - Return to main menu.")
    if (donor.lower() == "q" or donor.lower() == "quit"):
        startup_boot()
    elif (donor.lower() == "l" or donor.lower() == "list"):
        print_list()
        thank_you()
    else:
        cash = int(input("Please enter a donation amount or 'quit':"))
        if (cash.lower() == "q" or cash.lower() == "quit"):
            statup_boot()
        elif (response in contacts):
            history = contacts[donor]
            history.append(cash)
            print_letter()
        else:
            contacts.update({donor: cash})
            print_letter()


def generate_report():
    contacts_total = {}
    sorted_list = []
    for key, value in contacts:
        contacts_total.update({key: sum(value)})
    for key, value in sorted(contacts_total.iteritems(), key=lambda (k,v): (v,k)):
        storted_list.append(key)

