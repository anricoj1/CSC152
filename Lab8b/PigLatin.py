#PIG LATIN
#  Asks user to input a sentence
# conver words to Pig Latin
# moving first letter to end and add "ay" to the word
def main():
    words = str(input("Enter a Sentence: ")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
    print()

main()
