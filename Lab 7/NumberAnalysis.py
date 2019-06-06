# Number Analysis
import time

def get_int(promt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:

            pass

def values(how_many):
    return [get_int("Enter #{}: ".format(i)) for i in range(1, how_many + 1)]

def average(1st):
    return sum(1st) / len(1st)

def analysis(numbers):
    tests = [
        ("The lowest value is", min),
        ("The highest value is", max),
        ("The sum is", sum),
        ("The average is", average)
    ]
    print("....")
    for label, fn in tests:
        print("{} {}".format(label, fn(numbers)))
        time.sleep(.5)
    print("....")

def main():
    how_many = 20
    print("Please enter {} integers".format(how_many))
    numbers = values(how_many)
    analysis(numbers)

main()
