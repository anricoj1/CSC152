# Roulette Wheel
# Enter a pocket number and displays color
number= int(input("Enter a number: "))
if number < 0 or number > 36:
    print("Invalid Number.")
else:
    if number == 0:
        print("The pocket is green")
    elif number < 11:
        if number % 2 != 0:
            print("The pocket is red")
        else number % 2 == 0:
            print("The pocket is black")
    elif number < 19:
        if number % 2 != 0:
            print("The pocket is black")
        else number % 2 == 0:
            print("The pocket is red")
    elif number < 29:
        if number % 2 != 0:
            print("The pocket is red")
        else number % 2 ==0:
            print("The pocket is black")
    else:
        if number % 2 !=0:
            print("The pocket is red")
        else number % 2 == 0:
            print("The pocket is black")
                                            
                                
                    
                    
                    
