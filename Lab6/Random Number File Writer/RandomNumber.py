# Random Number File Writer
# Write a program that writes a series of random numbers to a file
# numbers should be in range of 1 - 500
import random
afile = open("randomnum.txt", "w")

try:
    for i in range( int( input("How many random numbers?: "))):
        line = str( random.randint(1,500))
        afile.write(line)
        print(line)
except ValueError:

    afile.close()
    


