import random
from datetime import datetime
random.seed(datetime.now())

# Here we go again.
# one of the things I code each time I learn a language is a simple fighter program.
# Create two objects who are our fighters.  Both start with a number of hit points
# then the beat each other until one is dead.
# FIRST we need to get some randome seeding - make it easy and use the current date / time
# not truly random but for what I need to do - its close enough.


# Very easy create two variables, bob and sue.  Give them both 50 to represent their HP.
bob = 50
sue = 50
count = 0

while (bob > 0 and sue > 0):
    count += 1
    print ('Bob has ' + str(bob) + ' hp.')
    print ('Sue has ' + str(sue) + ' hp.')
    bobhit = random.randrange(7) # essentially 1d6
    suehit = random.randrange(7) 
    bob = bob - suehit 
    sue = sue - bobhit # they both get to hit even if they're below 0 hp
    print ('Bob hits Sue for ' + str(bobhit))
    print ('Sue hits Bob for ' + str(suehit))
if (bob > sue and bob > 0):
    print (f'Bob Wins in {count} rounds!')
elif (sue > bob and sue > 0):
    print (f'Sue Wins in {count} rounds!')
else:
    print (f'I guess we\'ll call it a draw!\nThe battle lasted {count} rounds!')