from datetime import date

today = date.today()
print('Today is: ', today)

print("Year: ", today.year)
print("Month: ", today.month)
print("Day: ", today.day)
print("Time", today.ctime())