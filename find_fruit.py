fruits= ['Apple', 'Coconut', 'Pineapple', 'Strawberry']
letter = input('Enter the first letter:')

selected_fruits =  [fruit for fruit in fruits if fruit.lower().startswith(letter.lower())]
if selected_fruits:
 print("Fruits starting with '{}':{}".format(letter, ",".join(selected_fruits)))
else:
 print("No fruits found starting with '{}'. Try another letter.".format(letter))