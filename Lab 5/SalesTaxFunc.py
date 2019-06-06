# Write a program that calculates and displays the county and state sales tax
# Using functions

#define price
def price():
    price = float(input('Enter the price of the purchase: '))

price()

# define state tax
def StateTax(price):
    state_sales_tax = .05
    return price * state_sales_tax
StateTax(price)

# define county tax
def CountyTax(price):
    county_sales_tax =  .025
    return price * county_sales_tax
CountyTax(price)

# displahy all  the totals 
def displayTotals(price):
    print("Original price", price)
    state_tax = calculateStateTax(price)
    print("State tax", state_tax)
    county_tax = calculateCountyTax(price)
    print("County tax", county_tax)
    print("Total", price + state_tax + county_tax)

displayTotals(price)

    
# Im not very sure why this wont run properly...i dont see another way i could
# use functions to not get an TypeError
