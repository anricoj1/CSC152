# use nested loops to draw pattern
# for loop
for row in range(6):
    print("#", end="",sep="")
    for spaces in range(row):
        print(" ", end="", sep="")
        print("#", sep="")
