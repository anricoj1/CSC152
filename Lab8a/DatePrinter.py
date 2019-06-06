# Date Printer
# Write a program that reads a string from thr user
# mm/dd/yyyy
# prints March 12, 2017
def main():
    date = input("Enter the date mm/dd/yy: ")
    date_list = date.split()

    print(date_list)

    mm = date_list[1,12]
    dd = date_list[1,31]
    yyyy = date_list[0,2000000]

    print(mm.upper(), ".", dd.upper(), ".", yyyy.upper())

main()


