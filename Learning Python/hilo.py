low = 1 
high = 1023

print(f"Please think of a number between {low} and {high}")
input("PRESS ENTER TO BEGIN")

guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}.  Should I guess (h)igher (l)ower or (c)orrect ".format(guess)).casefold()

    if high_low == "h":
        # guess higher
        low = guess + 1
    
    elif high_low == "l":
        high = guess - 1

    elif high_low == "c":
        print(f"I got it in {guesses} guesses!")
        break
    else:
        print("You are a terrible person")

    guesses += guesses
else: 
    print(f"You thought of the number {low}")
    print(f"I've got it in {guesses} guesses!")