# Exception Handling
# Modify exercise 6 so habndles IOError exceptions
def main():
    try:
        numbersFile = open( "numbers.txt", "r" )
    except IOError as errorGenerated:
        print( "File not found: ", errorGenerated )
    else:
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
