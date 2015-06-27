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
            print(name)
        thank_you()
    elif (donor in contacts[0::3]):
        print(donor, "selected")
        # confirms that user made right choice
        process_cash(donor)
        startup_boot()
    else:
        contacts.extend([donor, [], 0])
        print("Adding %s to donation list (Pending)..." % donor)
        # Lets user know that new entry was added
        process_cash(donor)
        startup_boot()


def print_letter(donor, cash):
    """Prints letter, using 'donor' and 'cash' as parameters"""
    cash = money_formatter(cash)
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


def process_cash(donor):
    """Checks the donation, gives user the chance to back out"""
    cash = "cash"
    index = contacts.index(donor)
    while (not cash.replace('.', '', 1).isdigit()):
        # While loop activates if "cash" isn't an interget or decimal
        cash = input("Please enter a donation amount or type 'undo':")
        if (cash.lower()[:1] == "q"):
            quit()
        if (cash.lower()[:1] == "u"):
            if (contacts[index + 2] != 0):
                pass
            else:
                del contacts[index:(index + 3)]
                print(donor, "deleted from contacted list")
                # removes donor from contacts if user changes mind
            thank_you()
        if (cash[:1] == "$"):
            cash = cash[1:]
            print(cash)
            # removes "$" if "$" is used. We can re-test it in the next step
        if (not cash.replace('.', '', 1).isdigit()):
            print("Invalid Entry")
            # Error message if the final entry is not a number
    cash = float(cash)
    if ((cash * 100) % 1 != 0):
        # rejects entry if there are too many decimal places, i.e., "$43.433"
        print("Invalid Entry")
        process_cash(donor)
    else:
        contacts[index + 1].append(cash)
        contacts[index + 2] += cash
        # adds cash donation to donor history
        print_letter(donor, cash)
        # calls print function, using donor and cash as arguments


def money_formatter(amount, remove=0):
    """Format dollar amount as a formatted string with whole dollars"""
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


def report_line(name, total, number, average):
    """Takes raw inputs, calls on the formatters, and generates a line"""
    name = spaces_formatter(32, name)
    total = spaces_formatter(16, money_formatter(total, -3))
    number = spaces_formatter(6, number)
    average = spaces_formatter(16, money_formatter(average, -3))
    print(name, "|", total, "|", number, "|", average)


def sort_contacts(contacts, number_of_names):
    for i in range(number_of_names):
        i = i * 3 + 1
        contacts[i + 1] = sum(contacts[i])
    sorted_amounts = (sorted(contacts[2::3]))
    temp_list = []
    for amount in sorted_amounts:
        index = contacts.index(amount) - 2
        for i in range(3):
            temp_list.append(contacts[index + i])
    return temp_list


def generate_report():
    number_of_names = int(len(contacts) / 3)
    """Generates report of past donations"""
    print("-" * 79)
    report_line("Name :", "$Total :  ", "# :", "$Average :  ")
    # Prints out the title bar
    print("-" * 79)
    global contacts
    contacts = sort_contacts(contacts, number_of_names)
    for i in range(number_of_names):
        name = contacts[i * 3]
        total = contacts[i * 3 + 2]
        number = len(contacts[i * 3 + 1])
        average = total / number
        report_line(name, total, number, average)
        # for each name in the list, we generate a line
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
