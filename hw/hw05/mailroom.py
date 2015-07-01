contacts = {
    # constructing the contacts
    "Abe": [1, 2, 3],
    "Bob": [6, 7, 200],
    "Carl": [11],
    "Dave": [545545, 34325],
    "Eddie": [34, 656, 453, 34]
}


def startup_boot():
    """provides the main menu"""
    print("\n", "-" * 79)
    response = input("Welcome to Mailroom Madness\n"
        "\nChoose from the following:"
        "\nT - Send a (T)hank You and Print E-Mail"
        "\nR - Create a (R)eport"
        "\nquit - Quit the program\n\n> ")
    response = response.lower()[:1]
    # input only cares about the first letter
    if (response == "q"):
        quit()
    elif (response == "t"):
        thank_you()
    elif (response == "r"):
        generate_report("Total")
    else:
        print("Invalid entry.")
    startup_boot()
        # program reboots if entry is invalid


def thank_you():
    """Allows you to add entries contact list"""
    print("\n", "-" * 79)
    donor = input("Please enter a name, or choose from the following:"
        "\nlist - Print a list of previous donors"
        "\nquit - Return to main menu\n\n> ")
    if (donor.lower() == "q" or donor.lower() == "quit"):
        startup_boot()
    elif (donor.lower() == "l" or donor.lower() == "list"):
        generate_report("name")
        thank_you()
        # After list is presented, the prompt repeats itself
    elif (donor in contacts):
        pass
    else:
        contacts.update({donor: []})
        # Donor is added to contacts list if they are not there already
    process_cash(donor)


def donor_list():
    """Prints out every donor name in contact list"""
    print("-" * 79)
    for donor in sorted(contacts):
        # sorted command provides names in alphabetical order
        print(donor)


def process_cash(donor):
    """Checks the donation, gives user the chance to change names"""
    cash = "cash123!"
    while (not cash.replace('.', '', 1).isdigit()):
        # While loop activates if "cash" isn't an interget or decimal
        print("\n", "-" * 79)
        cash = input("Please enter a donation amount for %s, list donors, "
            "switch to different a donor, or 'quit':\n\n> $" % donor)
        if (cash.lower() == "q" or cash.lower() == "quit"):
            delete_new_donor(donor)
            startup_boot()
        elif (cash.lower() == "l" or cash.lower() == "list"):
            generate_report("name")
            process_cash(donor)
        elif (cash.replace('.', '').isalpha()):
            # Assumes that cash input is a donor if there are no digits
            delete_new_donor(donor)
            # Deletes current donor from contacts if donor is new
            if (cash in contacts):
                pass
            else:
                contacts.update({cash: []})
                # if cash input is a new donor, then we update the contacts
            process_cash(cash)
            # We now reset the cash prompt with a new donor
        elif (not cash.replace('.', '', 1).isdigit()):
            print("Invalid Entry")
            # Finally, error message if the final entry is not a number
    cash = float(cash)
    if ((cash * 100) % 1 != 0):
        # rejects entry if there are too many decimal places, i.e., "$43.433"
        print("Invalid Entry")
        process_cash(donor)
    else:
        contacts[donor].append(cash)
        # adds cash donation to donor history
        print_letter(donor, cash)
        input("Press Enter to continue...")
        startup_boot()
        # calls print function, using donor and cash as arguments


def delete_new_donor(donor):
    if (not contacts[donor]):
        # Returns "True" if donor has no prior donation history
        del contacts[donor]
        print(donor, "deleted from contacts list")


def print_letter(donor, cash):
    """Prints letter, using 'donor' and 'cash' as parameters"""
    print("-" * 79)
    print("Constructing letter...")
    print("-" * 79)
    print ("Dear {0},\n\n"
        "Thank you so much for your kind donation of {1}. We here at the "
        "Foundation for Homeless Whales greatly appreciate it. Your money "
        "will go towards creating new oceans on the moon for whales to live"
        "in.\n\nThanks again,\n\nJim Grant\n\nDirector, F.H.W.".format(
        donor, money_formatter(cash)))


def money_formatter(amount):
    """Format dollar amount as a formatted string with $ and commas"""
    amount = "$%.2f" % amount
    # rounds the amount to an integer, then converts it to a string
    if (len(amount) > 7):
        amount = amount[:-6] + "," + amount[-6:]
    if (len(amount) > 11):
        amount = amount[:-10] + "," + amount[-10:]
    if (len(amount) > 15):
        amount = amount[:-14] + "," + amount[-14:]
    return amount
        # adds commas when appropriate



def generate_report(sort_method):
    """Generates report of past donations"""
    contacts_total = {}
    print("-" * 79)
    print("Name: |".rjust(25), "$Total: |".rjust(20), "#: |".rjust(10), "$Average: |".rjust(20))
    # Prints out the title bar
    sorted_list = []
    # declares blank dictionary and list
    for key in contacts:
        contacts_total.update({key: sum(contacts[key])})
        # For each entry in original contacts, we now add a new dictionary
        # entry in the contacts_total.  contacts_total entries still have the
        # same key. but the value is a total sum rather than a list of entries.
    if (sort_method == "name"):
        for donor in sorted(contacts):
            sorted_list.append(donor)
    else:
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
        donations_total = money_formatter(donations_total)[:-3] + " |"
        donations_number = str(donations_number) + " |"
        donations_average = money_formatter(donations_average)[:-3] + " |"
        name = name  + " |"
        print(name.rjust(25), donations_total.rjust(20),
            donations_number.rjust(10), donations_average.rjust(20))
        # for each name in the list, we generate a line


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
