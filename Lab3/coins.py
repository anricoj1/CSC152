nbrCoins = int(input("Enter The Number Of Coins"))
print()

penny = 1
nickle = 5
dime = 10
quarter = 25

Penny = int(input("Please Enter The Number Of Pennies You Desire: "))
print()
Nickle = int(input("Please Enter The Number Of Nickles You Want: "))
print()
Dime = int(input("Please Enter The Number Of Dimes You’d Like: "))
print()
Quarter = int(input("Please Enter The Number Of Quarters You Want: "))

CoinTotal = Penny + Nickle + Dime + Quarter
TotalMoney = Penny  *  penny + Nickle * nickle + Dime * dime + Quarter * quarter

if TotalMoney == 100 and nbrCoins == CoinTotal:
	print("You Win!")
else :
    print("Sorry You Lost")
