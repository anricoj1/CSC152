#Initals
# Ask user for FULL NAME
# display initals J.M.A
def main():
    name = input("Type your FULL NAME and press ENTER/RETURN: ")
    name_list = name.split()

    print(name_list)

    first = name_list[0][0]
    second = name_list[1][0]
    last = name_list[2][0]

    print(first.upper(),".",second.upper(),".", last.upper())

main()
