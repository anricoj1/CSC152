def kilo():
    kilo = float(input("Enter distance in kilometers: "))
    return kilo

def miles(kilo):
    miles = kilo * 0.6214
    return miles

def main():
    print("This program converts kilometers to miles.")
    print(format(miles), '.2d', "miles")

main()
