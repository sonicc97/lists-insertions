food = ['KingBurger', 'Patato', 'Pizza', 'RedBull', 'HotDog']
print('This is food:')
print(food)
remove = input('What food to remove?')
try:
 food.remove(remove)
 print('This is the new food list!')
 print(food)
except ValueError:
 print('Item not found!')