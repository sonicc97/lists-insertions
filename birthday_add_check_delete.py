# This program contains a dictionary in which the names and birthdays of friends will be stored
# Global constants for menu selection
LOOK = 1
ADD = 2
CHANGE = 3
DELETE = 4
STOP = 5

# Main function
def main():
# We create an empty dictionary
    birthdays = {}
# We initialize a variable for the user's choice
    choice = 0
    while choice != STOP:
# We take the user's choice
        choice = user_choice()

# We are processing the selection
        if choice == LOOK:
            check(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)
        else:
            print('Program termination')



def user_choice():
    print()
    print('Friends and their birthdays')
    print('---------------------------')
    print('1. Check birthday')
    print('2. Add new birthday')
    print('3. Change birthday')
    print('4. Delete birthday')
    print('5. Stop the program')
    print()

# Enter the user's choice
    choice = int(input('Enter your choice'))

# Selection validation
    while choice < LOOK or choice > STOP:
        choice = int(input('Enter a valid choice'))

# Returns the user's choice.
    return choice

# LOOK function searches birthday based on name
def check(birthdays):
# We take the name
    name = input('Enter a name:')

# We look in the dictionary
    print(birthdays.get(name, 'Not found.'))

# The function add a new entry to the birthdays directory
def add(birthdays):
# We add name and birthday
    name = input('Enter a name:')
    birthdays = input('Enter a birthday:')

# If the name does not exist, we add it
    if name not in birthdays:
        birthdays[name] = birthdays
    else:
        print('That entry already exists.')

# The change function modifies an existing entry in the dictionary
def change(birthdays):
# We check if the name is in the dictionary
    name = input('Enter a name:')

    if name in birthdays:
# Enter a new birthday
        birthdays = input('Enter a new birthday:')

# We are updating the entry
        birthdays[name] = birthdays
    else:
        print('The entered name was not found.')

 # The DELETE function deletes the existing entry from the 'birthdays' dictionary
def delete(birthdays):
#We take the name
    name = input('Enter a name:')
 
# If the name is found delete the entry.
    if name in birthdays:
        del birthdays[name]
    else:
        print('Name not found!')

# Call the main function.

main()