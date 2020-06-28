# TODO - input validation

import random
from datetime import datetime
random.seed(datetime.now())
difficulty = int(input("Please enter the highest number you want to guess up to: "))
answer = random.randrange(1,difficulty)
guess = int(input("Please enter your guess for the guessing game between 1 and {}\n".format(difficulty)))
count = 1

while (guess != answer):
    if guess > answer:
        print("Too High!  Go lower!")
    else:
        print("Too Low!  Higher!")
    count = count + 1
    guess = int(input("Next guess: "))

print("Great job!  The number is {} and it took you {} tries!".format(answer, count))