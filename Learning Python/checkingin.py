# `in` is used in sequences
# Character strings are a type of sequence

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

# the casefold ensures everything is in the lower case and takes care
# of languages such as German which have a different case 

if letter in parrot.casefold():
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter.")