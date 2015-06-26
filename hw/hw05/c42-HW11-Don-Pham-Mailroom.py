# Dictionary sorting guide: http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
# Reverse order: http://stackoverflow.com/questions/5455606/how-to-reverse-order-of-keys-in-python-dict
# http://stackoverflow.com/questions/674509/how-do-i-iterate-over-a-python-dictionary-ordered-by-values

contacts = {
    # constructing the contacts
    "Abe": [1, 2, 3, 4, 5],
    "Bob": [6, 7, 8, 9, 10],
    "Carl": [11, 12, 13, 14, 15]
}


def startup_boot():
    """provides the main menu"""
    print("----------------------------")
    print("Welcome to Mailroom Madness")
    print("Choose from the following:")
    print("T - Send a (T)hank You and Print E-Mail")
    print("R - Create a (R)eport")
    response = input("quit - Quit the program: ")
    response = response.lower()[:1]
    # input only cares about the first letter
    if (response == "q"):
        quit()
    elif (response == "t"):
        thank_you()
    elif (response == "r"):
        generate_report()
    else:
        print("Invalid entry.")
        startup_boot()
        # program reboots with invalid entry


def thank_you():
    """Allows you to add entries contact list"""
    print("----------------------------")
    print("Let's create a letter!")
    print("Please enter a name, or choose from the following:")
    print("list - Print a list of previous donors")
    donor = input("back - Return to main menu: ")
    if (donor.lower() == "b" or donor.lower() == "back"):
        startup_boot()
    if (donor.lower() == "q" or donor.lower() == "quit"):
        quit()
    elif (donor.lower() == "1" or donor.lower() == "list"):
        print("----------------------------")
        for donor in sorted(contacts):
            # sorted command provides names in alphabetical order
            print(donor)
        thank_you()
    elif (donor in contacts):
        print(donor, "selected")
        # confirms that user made right choice
        process_cash(donor)
        startup_boot()
    else:
        contacts.update({donor: []})
        print("Adding", donor, "to donation list (Pending)...")
        # Lets user know that new entry was added
        process_cash(donor)
        startup_boot()


def print_letter(donor, cash):
    """Prints letter, using 'donor' and 'cash' as parameters"""
    print("Thank you, %s, for donating $%.2f" % (donor, cash))


def process_cash(donor):
    """Checks the donation, gives user the chance to back out"""
    cash = "cash"
    while (not cash.replace('.', '', 1).isdigit()):
        # While loop activates if "cash" isn't an interget or decimal
        cash = input("Please enter a donation amount or type 'undo':")
        if (cash.lower()[:1] == "q"):
            quit()
        if (cash.lower()[:1] == "u"):
            if (contacts[donor]):
                pass
            else:
                del contacts[donor]
                print(donor, "deleted from contacted list")
                # removes donor from contacts if user changes mind
            thank_you()
        if (cash[:1] == "$"):
            cash = cash[1:]
            print(cash)
            # removes "$" if "$" is used. We can re-test it in the next step
        if (not cash.replace('.', '', 1).isdigit()):
            print("Invalid Entry")
            # let's user know that entry is still invalid
    cash = float(cash)
    if ((cash * 100) % 1 != 0):
        # rejects entry if there are too many decimal places, i.e., "$43.433"
        print("Invalid Entry")
        process_cash(donor)
    contacts[donor].append(cash)
    # adds cash donation to donor history
    print_letter(donor, cash)
    # calls print function, using donor and cash as arguments


def money_formatter(amount):
    """Format dollar amount as a formatted string with whole dollars"""
    amount = str(int(amount))
    # rounds the amount to an integer, then converts it to a string
    if (len(amount) > 3):
        amount = amount[:-3] + "," + amount[-3:]
    if (len(amount) > 7):
        amount = amount[:-7] + "," + amount[-7:]
    if (len(amount) > 7):
        amount = amount[:-12] + "," + amount[-12:]
    amount = (15 - len(amount) * " ") + "$" + amount


def generate_report():
    """Generates report of past donations"""
    contacts_total = {}
    sorted_list = []
    # declares blank dictionary and list
    for key in contacts:
        contacts_total.update({key: sum(contacts[key])})
        # For each entry in original contacts, we now add a new dictionary
        # entry in the contacts_total.  contacts_total entries still have the
        # same key. but the value is a total sum rather than a list of entries.
    for item in sorted(contacts_total.items(), key=lambda x: x[1]):
        sorted_list.append(item[0])
        # Code sorts the contacts_total dictionary, then iterates through them.
        # For each iteration, it adds the name of the key to sort_list, which
        # we use to determine the order for the next step.
    for name in sorted_list:
        donations_total = contacts_total[name]
        donations_number = len(contacts[name])
        donations_average = (donations_total / donations_number)
        print("----------------------------")
        print(name, donations_total, donations_number, donations_average)
    startup_boot()


startup_boot()
