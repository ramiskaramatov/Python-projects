import os.path


# algorithm adjusts the entered phone number to the UK format
def format_phone(phone):
    ph = ''
    for i in phone:
        if i.isdigit():
            ph += i
    if len(ph) in (10, 11):
        if len(ph):
            ph = ph[0:]
        return '+44 (' + ph[0:1] + ')' + ph[1:5] + ' ' + ph[5:]
    return 'Please enter your correct contact number\n'


# algorithm adds the number to the end of the name
numbers = '0123456789'


def increment(s):
    out = ''
    number = ''

    for c in s:
        if c in numbers:
            number += c
        else:
            if number != '':
                out += str(int(number) + 1)
                number = ''
            out += c

    if number != '':
        out += str(int(number) + 1)
        number = ''

    return out


def welcome():
    entry = input("""        C O N T A C T   B O O K

        1. ALL ENTRIES
        2. ADD ENTRY
        3. FIND ENTRY
        4. EXIT

        Select one of the following options: """)
    print("")
    return entry


def directory():
    # infile = 'Phonebook.txt'
    while True:

        entry = welcome()

        # Checks if the phonebook contains any entries
        # Prints the phonebook in an alphabetic order and only unique entries
        if entry == '1':
            if os.path.getsize('Phonebook.txt') > 0:
                with open('Phonebook.txt', 'r') as file:
                    for line in sorted(set(file)):
                        print(line)
            else:
                print('PHONEBOOK IS EMPTY... \nTo add a contact, select option 2\n')

        # ADD ENTRY
        elif entry == '2':

            name = input("Entre FULL NAME: ").capitalize()

            # Checks if name already exists, it's duplicated with '*'
            with open('Phonebook.txt', 'r') as file:
                for line in file.readlines():
                    if name in line:
                        name = increment(name + '*')  # name += name

            phone_number = format_phone(input("Enter PHONE NUMBER: "))

            # Checks if the phone number already exists
            i = 0
            file = open('Phonebook.txt', 'r')
            for line in file.readlines():
                if phone_number in line:
                    i += 1
            file.close()

            if i == 0:
                new_entry = name + '\t' + phone_number + '\n'
                file = open('Phonebook.txt', 'a')
                file.write(new_entry)
                file.close()
                print('\n...this contact is successfully added\n')
            else:
                print('\n...this phone number already exists\n')

        # FIND ENTRY
        elif entry == '3':
            name_to_search = input('Enter the name you wish to FIND: ').capitalize()
            print('')

            if os.path.getsize('Phonebook.txt') > 0:
                with open('Phonebook.txt', 'r') as file:
                    for line in file.readlines():
                        if name_to_search in line:
                            print('...found -->', line, '\n')
                    if name_to_search not in line:
                        print("\n...this contact does NOT exist!"
                              "\n...return to the main menu to enter the contact\n")
            else:
                print('The phonebook is empty')

            file.close()


        # EXIT
        elif entry == '4':
            print("\nSee you soon!")
            break
        # Error Message
        else:
            print("PLEASE ENTER A VALID CHOICE\n")


directory()
