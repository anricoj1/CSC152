# Write a program that asks user for age
age=int(input("Please enter a persons age: "))
if age <= 1:
    classified = "infant"
elif age > 1 and age < 13:
    classified = "child"
elif age >= 13 and age < 20:
    classified = "teenager"
elif age >= 20:
    classified = "child"
#output age
print("Age", age, "is", classified)
        

    
    
