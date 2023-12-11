test_names = "Peter Brian Chris Stewie Glenn Joe Mort Adam Herbert Tom"
name1 = input("Enter first name to test: ")
name2 = input("Enter second name to test: ")
print('''Choose an option to test names:
        1: 1st and 2nd name are in the string
        2: 1st or 2nd name are in the string
        3: 1st name is and 2nd name is not in the string
    ''')
choice = int(input("Enter a choice: "))

if choice == 1:
    if name1 in test_names and name2 in test_names:
        print(f'Both {name1} and {name2} are in the string.')
    else:
        print('Both names are not in the string.')
elif choice == 2:
    if name1 in test_names or name2 in test_names:
        print('At lest one name is in the string.')
    else:
        print('Neither name is in the string.')
elif choice == 3:
    if name1 in test_names and name2 not in test_names:
        print(f'The name {name1} is in the string, while {name2} is not in the string.')
    else:
        print('The combination of names in and not in the string could not be computed.')
else:
    print("You chose poorly.")