# Dictionary sorting guide: http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
# Reverse order: http://stackoverflow.com/questions/5455606/how-to-reverse-order-of-keys-in-python-dict

contacts = {
    "Abe": [1, 2, 3, 4, 5],
    "Bob": [6, 7, 8, 9, 10],
    "Carl": [11, 12, 13, 14, 15]
}


def startup_boot():
    print("----------------------------")
    print("Welcome to Mailroom Madness")
    print("Choose from the following:")
    print("T - Send a (T)hank You and Print E-Mail")
    print("R - Create a (R)eport")
    response = input("quit - Quit the program: ")
    response = response[:1]
    response = response.lower()
    if (response == "q"):
        quit()
    elif (response == "t"):
        thank_you()
    elif (response == "r"):
        generate_report()
    else:
        print("Invalid entry.")
        startup_boot()


def thank_you():
    print("----------------------------")
    print("Please enter a name, or choose from the following:")
    print("list - Print a list of previous donors")
    donor = input("quit - Return to main menu: ")
    if (donor.lower() == "q" or donor.lower() == "quit"):
        startup_boot()
    elif (donor.lower() == "l" or donor.lower() == "list"):
        print("----------------------------")
        for donor in sorted(contacts):
            print(donor)
        thank_you()
    else:
        cash = int(input("Please enter a donation amount or 'quit': "))
        if (cash.lower() == "q" or cash.lower() == "quit"):
            statup_boot()
        elif (donor in contacts):
            history = contacts[donor]
            history.append(cash)
            print_letter()
        else:
            contacts.update({donor: cash})
            print_letter()


def print_list():
    print("print_list")


def print_letter():
    print("print_letter")


def generate_report():
    contacts_total = {}
    sorted_list = []
    for key in contacts:
        contacts_total.update({key: sum(contacts[key])})
    for item in sorted(contacts_total.items(), key=lambda x: x[1]):
        sorted_list.append(item[0])
    for name in sorted_list:
        donations_total = contacts_total[name]
        donations_number = len(contacts[name])
        donations_average = donations_total / donations_number
        print("----------------------------")
        print(name, donations_total, donations_number, donations_average)
    startup_boot()


startup_boot()
