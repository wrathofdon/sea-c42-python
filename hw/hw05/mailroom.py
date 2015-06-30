# Dictionary sorting guide: http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
# Reverse order: http://stackoverflow.com/questions/5455606/how-to-reverse-order-of-keys-in-python-dict
# http://stackoverflow.com/questions/674509/how-do-i-iterate-over-a-python-dictionary-ordered-by-values

contacts = {
    # constructing the contacts
    "Abe": [1, 2, 3],
    "Bob": [6, 7],
    "Carl": [11]
}


def startup_boot():
    """provides the main menu"""
    response = input("Welcome to Mailroom Madness\n"
        "\nChoose from the following:"
        "\nT - Send a (T)hank You and Print E-Mail"
        "\nR - Create a (R)eport"
        "\nquit - Quit the program\n> ")
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
    donor = input("Please enter a name, or choose from the following:"
        "list - Print a list of previous donors"
        "quit - Return to main menu\n> ")
    if (donor.lower() == "q" or donor.lower() == "quit"):
        startup_boot()
    elif (donor.lower() == "l" or donor.lower() == "list"):
        print("----------------------------")
        for donor in sorted(contacts):
            # sorted command provides names in alphabetical order
            print(donor)
        thank_you()
    elif (donor in contacts):
        pass
        # confirms that user made right choice
    else:
        contacts.update({donor: []})
        # Lets user know that new entry was added
    process_cash(donor)
    startup_boot()


def print_letter(donor, cash):
    """Prints letter, using 'donor' and 'cash' as parameters"""
    print("-" * 79)
    print("Constructing letter...")
    print("-" * 79)
    print ("Dear %s,\n\n"
        "Thank you so much for your kind donation of $%.2f. We here at"
        "the Foundation for Homeless Whales greatly appreciate it. Your "
        "money will go towards creating new oceans on the moon for whales to "
        "live in.\n\nThanks again,\n\nJim Grant\n\nDirector, F.H.W."
        % (donor, cash))
    input("Press Enter to continue...")


def process_cash(donor):
    """Checks the donation, gives user the chance to back out"""
    cash = "cash"
    while (not cash.replace('.', '', 1).isdigit()):
        # While loop activates if "cash" isn't an interget or decimal
        cash = input("Please enter a donation amount or 'quit':\n> $")
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
        if (not cash.replace('.', '', 1).isdigit()):
            print("Invalid Entry")
            # Error message if the final entry is not a number
    cash = float(cash)
    if ((cash * 100) % 1 != 0):
        # rejects entry if there are too many decimal places, i.e., "$43.433"
        print("Invalid Entry")
        process_cash(donor)
    else:
        contacts[donor].append(cash)
        # adds cash donation to donor history
        print_letter(donor, cash)
        # calls print function, using donor and cash as arguments


def money_formatter(amount):
    """Format dollar amount as a formatted string with whole dollars"""
    if (type(amount) == str):
        return spaces_formatter(16, amount)
        # This is so I can use a regular string in the title bar
    amount = "$" + str(int(amount))
    # rounds the amount to an integer, then converts it to a string
    if (len(amount) > 4):
        amount = amount[:-3] + "," + amount[-3:]
    if (len(amount) > 8):
        amount = amount[:-7] + "," + amount[-7:]
    if (len(amount) > 12):
        amount = amount[:-11] + "," + amount[-11:]
        # adds commas when appropriate
    return spaces_formatter(16, amount)


def spaces_formatter(total, string):
    """Adds spaces so that  strings will take up fixed amount of space"""
    string = str(string)
    limit = total - 2
    if (len(string) > limit):
        string = string[:limit]
        # This is in case of a very, very long name
    string = ((total - len(string)) * " ") + string
    return string


def report_line(name, total, number, average):
    """Takes raw inputs, calls on the formatters, and generates a line"""
    name = spaces_formatter(32, name)
    total = money_formatter(total)
    number = spaces_formatter(6, number)
    average = money_formatter(average)
    print(name, "|", total, "|", number, "|", average)


def generate_report():
    """Generates report of past donations"""
    contacts_total = {}
    print("-" * 79)
    report_line("Name:", "$Total", "#", "$Average")
    # Prints out the title bar
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
    print("-" * 79)
    for name in sorted_list:
        donations_total = contacts_total[name]
        donations_number = len(contacts[name])
        donations_average = (donations_total / donations_number)
        report_line(name, donations_total, donations_number, donations_average)
        # for each name in the list, we generate a line
    startup_boot()


startup_boot()
print(spaces_formatter(5, "1"))


if __name__ == '__main__':
    assert(spaces_formatter(5, "test") == " test")
    assert(spaces_formatter(7, "test") == "  test")
    assert(spaces_formatter(8, "test") == "   test")
    assert(spaces_formatter(9, "test") == "    test")
    assert(money_formatter(16, "9999999999") == "  $9,999,999,999")
    assert(money_formatter(16, "9999999999.4342") == "  $9,999,999,999")
    assert(money_formatter(16, "1.04342") == "              $1")
    assert(money_formatter(16, "1") == "              $1")
