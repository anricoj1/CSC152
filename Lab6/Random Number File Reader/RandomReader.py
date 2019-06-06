# Write a program that reads the random numbers from the file
# display numbers, and then display.....
#Total
# numbers of random numbers read from the file
import random

def main():
    afile = open("randnumbers.txt", "r")

    line == afile.readline()
    number = 0
    total = 0

while line:
    number += int(line)
    total += 1
    line = afile.readline().rstrip("\n")

print("The total of the number: " + str(total))
print("Total count of numbers read from file: " + str(number))
more = input("Do you want to run again?: (Y/N): ")

afile.close()
main()

    
