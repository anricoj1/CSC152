# declare constant
MONTHS = 12

# declarce variables
monthly_rainfall = []
years = int(input("How many years of rainfall?: "))
print("You choose",years , "years.")

# define nested loop to gather rainfall data
for time in range(years):
    for month in range(1,13):
        rain = float(input("Enter total inches of rain for month {}:  ".format(month)))
        monthly_rainfall.append(rain)
        

total_months = years * MONTHS

# calculate and print results
print("Total months of rainfall: " + str(total_months))    
print("Total inches of rainfall: " + str(sum(monthly_rainfall)))
print("Average inches of rainfall per month: " + str(sum(monthly_rainfall) / total_months))
