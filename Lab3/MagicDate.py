#Find the Magic Date
month= int(input("Enter a month number:" ))
if month < 1 or month > 12:
    print("The month cannot be less than 1 or greater than 12.")
day= int(input("Enter a day number: "))
if day < 1 or day > 31:
    print("The day cannot be less than 1 or greater than 31.")
year = int(input("Enter a year number: "))
if day < 0 or year > 99:
    print("The year cannot be less than 0 or greater than 99.")
if year == month*day:
    print("Magic Date")
else:
    print("Not a Magic Date")
