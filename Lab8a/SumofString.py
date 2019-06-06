# Sum of Digits in a string
# Write a program that asks the user to enter a series of single-digit numbers
# get the sum of that number
number = int(input("Enter numbers with no spaces: "))
sum = 0

while(number > 0):
    reminder = number % 10
    sum = sum + reminder
    number = number //10

print("\n Sum of the digits of the given number = %d" %sum)



    
