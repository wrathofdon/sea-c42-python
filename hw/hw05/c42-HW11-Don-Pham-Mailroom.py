# Dictionary sorting guide: http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
# Reverse order: http://stackoverflow.com/questions/5455606/how-to-reverse-order-of-keys-in-python-dict
# http://stackoverflow.com/questions/674509/how-do-i-iterate-over-a-python-dictionary-ordered-by-values

contacts = {
    "Abe": [1, 2, 3, 4, 5],
    "Bob": [6, 7, 8, 9, 10],
    "Carl": [11, 12, 13, 14, 15]
}


def startup_boot():
    print("----------------------------")
    print(contacts)
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
    donor = input("back - Return to main menu: ")
    if (donor.lower() == "b" or donor.lower() == "quit"):
        startup_boot()
    if (donor.lower() == "q" or donor.lower() == "quit"):
        quit()
    elif (donor.lower()[:1] == "l"):
        print("----------------------------")
        for donor in sorted(contacts):
            print(donor)
        thank_you()
    elif (donor in contacts):
        print(donor, " selected")
        process_cash(donor)
        startup_boot()
    else:
        contacts.update({donor: []})
        print("Adding ", donor, " to donation list (Pending)...")
        process_cash(donor)
        startup_boot()


def print_list():
    print("print_list")


def print_letter():
    print("print_letter")


def test_cash(cash):
    try:
        float(cash)
        print("valuetrue")
        return True
    except ValueError:
        print("valuefalse")
        return False


def process_cash(donor):
    cash = "cash"
    while (not test_cash(cash)):
        print(contacts)
        cash = input("Please enter a donation amount or 'back':")
        if (cash.lower()[:1] == "q"):
            quit()
        if (cash.lower()[:1] == "b"):
            if (contacts[donor]):
                pass
            else:
                del contacts[donor]
            thank_you()
        print(cash)
        if (cash[:1] == "$"):
            cash = cash[1:]
            print(cash)
    print("94")
    cash = float(cash)
    if (cash % 1 != 0):
        print("Rounding donation value to", int(cash))
    cash = int(cash)
    contacts[donor].append(cash)


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
        donations_average = round(donations_total / donations_number, 2)
        print("----------------------------")
        print(name, donations_total, donations_number, donations_average)
    startup_boot()


startup_boot()
