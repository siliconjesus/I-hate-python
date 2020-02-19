# first iteration - using one of my favorite operators (modulus) to clean up the mess.
from datetime import datetime

right_this_minute = datetime.today().minute

# the following line probably violates some sort of python principal regarding simplicity
# Modulus is essentially the remainder function - the way we learned
# division in school before we learn about decimals.  
# EXAMPLE: 5 ÷ 2 = 2r1
# in python we use % to get this - so 5 % 2 = 1.
# if the remainder is 1 - its 'true'
# if its zero - its 'false'
if (right_this_minute % 2):
    print("this minute seems a little odd.")
else:
    print("not an odd minute.")