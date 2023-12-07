import random
names = ['Sonic', 'Summer', 'Finland', 'Dota2', 'Winter', 'Basketball', 'Music', 'Skateboard']
choice = random.choice(names)
multiple_name_selection = random.choices(names, k=3)
print(choice)
print(multiple_name_selection)