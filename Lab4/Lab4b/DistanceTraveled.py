# Write a program that loops the distance travled to the amount of hours driving


# Ask for speed in mph
# Hoe many hours travel?
speed= input("What is the speed of the vehicle in mph?: ")
print(speed)
time= input("How many hours has it traveled?: ")
print(time)

print("Hour --- Distance Traveled")

for hour in range(1,2,):
    distance = speed * hour
    print(str(hour) + "        " + str(distance))


