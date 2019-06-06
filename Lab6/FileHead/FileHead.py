# File Head Display
def main():
    maxLines = 5
    lineRead = 0
    
    fileName = input("Please enter the file name: ")

    readFile = open( fileName, "r" )

    line = readFile.readline()
    lineRead = lineRead + 1

    while line != "" and lineRead <= maxLines:
        print( line.rstrip("\n") )
        line = readFile.readline()
        lineRead = lineRead + 1

    readFile.close()

main()

    
    
