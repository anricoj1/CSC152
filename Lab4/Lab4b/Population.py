# Write a program that predicts the approximate population
# Define information given
organisms = int(input("Starting number of organisms: "))
increase = int(input("Average daily increase: "))
days = int(input("Number of days to multiply: "))



print("Day    Population")
# Display table of data
for days in range(1, 11):
    organisms = organisms + organisms * increase / 100 
    print(str(days) + "         " + str(organisms))
    
