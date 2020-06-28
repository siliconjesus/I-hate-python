import random
from datetime import datetime
random.seed(datetime.now())

answer = random.randrange(1,10)
guess = int(input("Please enter your guess for the guessing game between 1 and 10\n"))
count = 0

while (guess != answer):
    if guess > answer:
        print("Too High!  Go lower!")
    else:
        print("Too Low!  Higher!")
    count = count + 1
    guess = int(input("Next guess: "))

print("Great job!  The number is {} and it took you {} tries!".format(answer, count))