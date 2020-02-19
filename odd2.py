from datetime import datetime

right_this_minute = datetime.today().minute

if (right_this_minute % 2):
    print("this minute seems a little odd.")
else:
    print("not an odd minute.")