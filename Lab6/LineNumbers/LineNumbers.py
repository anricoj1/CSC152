# Line Numbers
# Ask for a file to read 
# file: random.txt
def main():
    fileName = input(" Please enter a file name: ")

    fileRead = open( fileName, "r" )

    line = fileRead.readline()

    lineNumber = 1

    while line != "":
        print(str( lineNumber ) + ":", line.rstrip( "\n") )
        line = fileRead.readline()
        lineNumber = lineNumber + 1

main()
