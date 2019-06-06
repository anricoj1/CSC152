# Display colors and display an error if color isnt red, blue or yellow
color1= input("Primary color one. (red, blue, yellow): ")
color2= input("Primary color two. (red, blue, yellow): ")
if color1 == "red" and color2 == "blue" or color1 == "blue" and color2 == "red":
    print("Your result is purple")
elif color1 == "red" and color2 == "yellow" or color1 == "yellow" and color2 == "red":
    print("Your result is orange")
elif color1 == "blue" and color2 == "yellow" or color1 == "yellow" and color2 == "blue":
    print("your result is green")
else:
    print("Error")
