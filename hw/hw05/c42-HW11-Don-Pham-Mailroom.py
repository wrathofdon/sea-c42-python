# Dictionary sorting guide: http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
# Reverse order: http://stackoverflow.com/questions/5455606/how-to-reverse-order-of-keys-in-python-dict
# http://stackoverflow.com/questions/674509/how-do-i-iterate-over-a-python-dictionary-ordered-by-values

contacts = ["Abe", [1, 2, 3], 6, "Bob", [6, 7], 44413, "Carl", [11], 3311]
"""This is a variant of the assignment that only uses lists without
dictionaries.  Each person in the contacts list has three elements: Name,
an internal list containing donation history, and the donation totals."""


def startup_boot():
    """provides the main menu"""
    print("-" * 79)
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
    print("-" * 79)
    print("Let's create a letter!")
    print("Please enter a name, or choose from the following:")
    print("list - Print a list of previous donors")
    donor = input("back - Return to main menu: ")
    if (donor.lower() == "b" or donor.lower() == "back"):
        startup_boot()
    if (donor.lower() == "q" or donor.lower() == "quit"):
        quit()
    elif (donor.lower() == "l" or donor.lower() == "list"):
        print("-" * 79)
        for name in sorted(contacts[0::3]):
            # sorts & every third item in contacts list, which are the names
            print(name)
        thank_you()
    elif (donor in contacts[0::3]):
        # checks to see if name is already in list
        print(donor, "selected")
        # confirms that user made right choice, then calls for cash
        process_cash(donor)
        startup_boot()
    else:
        contacts.extend([donor, [], 0])
        print("Adding %s to donation list (Pending)..." % donor)
        # Lets user know that new entry was added, then calls for cash
        process_cash(donor)
        startup_boot()


def process_cash(donor):
    """Checks the donation, gives user the chance to back out"""
    index = contacts.index(donor)
    # code searches for coordinates of donor for later use
    cash = "cash"
    # cash is declared as invalid from start, in order to launch promp
    while (not cash.replace('.', '', 1).isdigit()):
        # While loop activates if "cash" isn't an interget or decimal
        cash = input("Please enter a donation amount or type 'undo':")
        # user is given chance to change mind
        if (cash.lower()[:1] == "q"):
            quit()
        if (cash.lower()[:1] == "u"):
            if (contacts[index + 2] != 0):
                pass
                # old donor information is preserved if user changes mind
            else:
                del contacts[index:(index + 3)]
                print(donor, "deleted from contacted list")
                # removes new donor from contacts if user changes mind
            thank_you()
            # if user changes mind, they can now type a different donor
        if (cash[:1] == "$"):
            cash = cash[1:]
            print(cash)
            # removes "$" if "$" is used. We can re-test it in the next step
        if (not cash.replace('.', '', 1).isdigit()):
            print("Invalid Entry")
            # Error message if the final entry is not a number
    cash = float(cash)
    # accepts payment in pennies
    if ((cash * 100) % 1 != 0):
        # rejects entry if there are too many decimal places, i.e., "$43.433"
        print("Invalid Entry")
        process_cash(donor)
    else:
        contacts[index + 1].append(cash)
        contacts[index + 2] += cash
        # adds cash donation to donor history & to the total, which are in the
        # cells adjacent to the names
        print_letter(donor, cash)
        # calls print function, using donor and cash as arguments


def print_letter(donor, cash):
    """Prints letter, using 'donor' and 'cash' as parameters"""
    cash = money_formatter(cash)
    # calls for the money formmatter, which adds commas to large dollar amounts
    print("-" * 79)
    print("Constructing letter...")
    print("-" * 79)
    print ("Dear %s,\n\n"
        "Thank you so much for your kind donation of %s. We here at"
        "the Foundation for Homeless Whales greatly appreciate it. Your "
        "money will go towards creating new oceans on the moon for whales to "
        "live in.\n\nThanks again,\n\nJim Grant\n\nDirector, F.H.W."
        % (donor, cash))
    input("Press Enter to continue...")


def money_formatter(amount, remove=0):
    """Format dollar amount as a formatted string with whole dollars"""
    # "remove" is optional parameter that cuts off the end of the final string.
    # if set to -3, it will convert $X.YZ to $X, useful for final report.
    if (type(amount) == str):
        return spaces_formatter(16, amount)
        # This is so I can use a regular string in the title bar
    amount = "$%.2f" % amount
    # rounds the amount to an integer, then converts it to a string
    if (len(amount) > 7):
        amount = amount[:-6] + "," + amount[-6:]
    if (len(amount) > 11):
        amount = amount[:-10] + "," + amount[-10:]
    if (len(amount) > 15):
        amount = amount[:-14] + "," + amount[-14:]
        # adds commas when appropriate
    amount = amount[0:(len(amount) + remove)]
    # "remove" is optional parameter to remove pennies from dollar amounts
    return amount


def spaces_formatter(total, string):
    """Adds spaces so that  strings will take up fixed amount of space"""
    string = str(string)
    limit = total - 2
    if (len(string) > limit):
        string = string[:limit]
        # This is in case of a very, very long name
    string = ((total - len(string)) * " ") + string
    return string


def report_line(name, total, number, average, remove=0):
    """Takes raw inputs, calls on the formatters, and generates a line"""
    name = spaces_formatter(32, name)
    total = spaces_formatter(16, money_formatter(total, remove))
    number = spaces_formatter(6, number)
    average = spaces_formatter(16, money_formatter(average, remove))
    print(name, "|", total, "|", number, "|", average)


def sort_contacts(contacts, number_of_names):
    """Sorts contacts list by total donation value"""
    for i in range(number_of_names):
        # number of names = len(contacts) / 3,
        i = i * 3 + 1
        # This starts at 1 and counts by 3, provides the donation history lists
        contacts[i + 1] = sum(contacts[i])
        # Takes the sum of each list and places the total in the next element
    temp_contacts = list(contacts)
    # We need to create a temporary copy of the contacts list we can edit
    # This is to prevent a potential issue where two names have the same total
    # In that case, the same name might get counted twice.
    # Now, the name is removed from the temporary copy, but not the original
    sorted_amounts = (sorted(contacts[2::3]))
    # this pulls the total values from the list and sorts them
    temp_list = []
    for amount in sorted_amounts:
        index = temp_contacts.index(amount) -2
        temp_list.extend(temp_contacts[index:(index + 3)])
        del temp_contacts[index:(index + 3)]
    return temp_list


def generate_report():
    """Generates report of past donations"""
    number_of_names = int(len(contacts) / 3)
    # counts the number of names in contacts list
    print("-" * 79)
    report_line("Name:", "$Total:  ", "#:", "$Average:  ")
    # Prints out the title bar
    # Spaces are added to offset remove in the report_line
    print("-" * 79)
    # prevents shadow variable
    temp_contacts = sort_contacts(contacts, number_of_names)
    for i in range(number_of_names):
        name = temp_contacts[i * 3]
        total = temp_contacts[i * 3 + 2]
        number = len(temp_contacts[i * 3 + 1])
        average = total / number
        report_line(name, total, number, average, -3)
        # for each name in the list, we generate a line
        # this is the only time the "remove" parameter is called
    startup_boot()


startup_boot()


"""if __name__ == '__main__':
    assert(spaces_formatter(5, "test") == " test")
    assert(spaces_formatter(7, "test") == "  test")
    assert(spaces_formatter(8, "test") == "   test")
    assert(spaces_formatter(9, "test") == "    test")
    assert(money_formatter(16, "9999999999") == "  $9,999,999,999")
    assert(money_formatter(16, "9999999999.4342") == "  $9,999,999,999")
    assert(money_formatter(16, "1.04342") == "              $1")
    assert(money_formatter(16, "1") == "              $1")"""
