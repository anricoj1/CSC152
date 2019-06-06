import random

random1 = random.randint(1, 250)
random2 = random.randint(1, 250)

def Question():
    global random1
    global random2
    userAnswer = int( input( "What is " + str(random1) + "+" + \
                             str( random2 ) + "?: "))
    return userAnswer

def checkAnswer( userAnswer ):
    global random1
    global random2

    correctAnswer = random1 + random2
    print()
    if userAnswer == correctAnswer:
        print("Correct!")
    else:
        print("That's wrong. The correct answer is", correctAnswer )


def main():
    userAnswer = Question()
    checkAnswer( userAnswer )

main()
