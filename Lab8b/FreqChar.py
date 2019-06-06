#Most Frequent Character
# Write a program that lets the user enter a string and displays the character
# That appears most frequently 
import collections
print("This programs finds the most commmon character in a string.......")
s = input("Enter a word: ")
print(collections.Counter(s).most_common(1)[0])
