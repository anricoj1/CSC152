# Write a program that asks the user to enter a distance in kilometers
# Then converts that distance to miles
# Miles = Kilometers x 0.6214
def kilo():
    kilometers = float(input("What is the distance in kilometers: "))
    return kilometers
 
def miles(kilometers):
    miles = kilometers * 0.6214
    return miles
 
def main():
    print("This program converts kilometers to miles.")
    km = kilo()
    k = miles(km)
    print(format(k, '.2f'))
    
    

main()

          
    




         
