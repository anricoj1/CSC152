# Stadium Seating
# Three seating categories
# Class A seats cost $ 20
# Class B cost $15
# Class C cost $10
# Write a program that asks how many tickets for each class of seats were sold

def ClassA( ClassATickets ):
    classASales = classATickets = 20
    return classASales

def ClassB( ClassBTickets ):
    classBSales = classBTickets = 15
    return classBSales

def ClassC( ClassCTickets ):
    classCSales = classCTickets = 10
    return classCSales

def TotalSales( classASales, classBSales, classCSales ):
    totalSales = classAsales + classBSales + classCSales
    return TotalSales

def SalesReport( classASales, classBSales, classCSales, TotalSales ):
    print("Class A Sales: $" + format( classASales, ",.2f"))
    print("Class B Sales: $" + format( classBSales, ",.2f"))
    print("Class C Sales: $" + format( classCSales, ",.2f"))
    print("Total Sales: $" + format( TotalSales, ",.2f"))
    print()
          
def main():
    ClassATickets = int(input(" How many tickets were bought for Class A: "))
    ClassBTickets = int(input(" How many tickets were bought for Class B: "))
    ClassCTickets = int(input(" How many tickets were bought for Class C: "))
    classASales = ClassA( ClassATickets )
    classBSales = ClassB( ClassBTickets )
    classCSales = ClassC( ClassCTickets )
    SalesReport( classASales, classBSales, classCSales,TotalSales)
    
main()
