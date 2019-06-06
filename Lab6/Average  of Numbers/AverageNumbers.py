# Average of Numbers
# Assume that file containes a series of intefers and is named "numbers.txt"
# Average all the numbers stored in file
def main():
    numbersFile = open( "numbers.txt", "r" )

    total = 0
    numberLines = 0
    line = numbersFile.readline()

    while line != "":
        numberLines += 1
        total += int( line )
        line = numbersFile.readline()

    average = total / numberLines

    print( "The average is", average )

main()

    
