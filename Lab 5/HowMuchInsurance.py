# How much insurance ?
# Write a program thart asks user to enter the replacement cost of a building
# Displays minimum amount of insurance he or she should buy
def replacement_cost():
    replacementCost = float(input("Enter the replacement cost of the building: "))

    return replacementCost

def min_insurance(replacementCost):
    minimumInsurance = ( 80 / 100 ) * replacementCost
    return minimumInsurance

def details( replacementCost, minimumInsurance ):
    print()
    print("You should insure your house for $" + \
          format(minimumInsurance, ",.2f") +  "because that's 80% of the" + \
          "replacement cost of your building, which is $" + \
          format( replacementCost, ",.2f"))

def main():
    replacementCost = replacement_cost()
    minimumInsurance = min_insurance(replacementCost)
    details(replacementCost, minimumInsurance)

main()


    

