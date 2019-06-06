#Ask user for an amount of packages
#Recieve the discount and total
quantity = int(input("Enter the number of packages purchased. "))
before_discount = quantity*99

if(quantity>9 and quantity<20):
    discount = before_discount*.20
    total = before_discount - discount
    print("If you buy {} package(s), your discount is ${} and your total is ${}.".format(quantity,discount,total))

elif(quantity>19 and quantity<50):
    discount = before_discount*.30
    total = before_discount - discount
    print("If you buy {} package(s), your discount is ${} and your total is ${}.".format(quantity,discount,total))

elif(quantity>49 and quantity<100):
    discount = before_discount*.40
    total = before_discount - discount
    print("If you buy {} package(s), your discount is ${} and your total is ${}.".format(quantity,discount,total))

elif(quantity>99):
    discount = before_discount*.50
    total = before_discount - discount
    print("If you buy {} package(s), your discount is ${} and your total is ${}.".format(quantity,discount,total))


