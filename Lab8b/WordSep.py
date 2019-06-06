# Word Separator
# Write a program that accepts an input and separates it into a sentence
my_string = input("Enter a sentence with no spaces: ")
i = 0
result = ""
for c in my_string:
    if c.isupper() and i > 0:
        result += " "
        result += c.lower()
    else:
        result += c
    i += 1
print(result)
