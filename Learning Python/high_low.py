import random
from datetime import datetime
random.seed(datetime.now())

difficulty = int(input("Please enter the highest number you want to guess up to: "))
answer = random.randrange(1,difficulty)

low = 1
high = difficulty

count = 1

while True:
    guess = low + (high - low) // 2
    if guess < answer:
        print(f"Guess was {guess} | Guess was LOW  | Guess Count is {count} ")
        low = guess + 1
    elif guess > answer:
        print(f"Guess was {guess} | Guess was HIGH | Guess Count is {count} ")
        high = guess - 1
    else:
        print("W I N N E R \n" * 2)
        print(f"The number was {guess} and it took me {count} tries to get it.")
        break
    count += 1