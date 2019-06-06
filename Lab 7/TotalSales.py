# Total Sales
# Write a program that asks user to enter stotes sales doe each day of the week
# Should be stored in a list
# Use a loop to caculate the total sales

def main():

    total = 0.0
    sales = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    index = 0

    days = ["Sunday", "Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday"]

    for index in range(7):

        print("Enter the amount of sales for", days[index])
        sales[index] = float(input("Enter the sales here: "))

        total += sales[index]

    print("The total sales for the weeks is $", format(total, ".2f"), sep= " ")

main()
