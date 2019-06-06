#Calories Burned
# Tredmill burns 4.2 cal per minute...
# loop to display number of calories after 10, 15, 20, 25, and 30 minutes
caloriesBurnedPer = 4.2

for numberOfMinutes in range( 10, 31, 5):
    numberOfCaloriesBurned = (numberOfMinutes / 1) * caloriesBurnedPerMinute
    print("You will burn", numberOfCaloriesBurned,"calories in",numberOfMinutes,"minutes")
    
    
