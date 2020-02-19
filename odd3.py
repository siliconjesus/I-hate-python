from datetime import datetime

if (datetime.today().minute % 2):
    print("this minute seems a little odd.")
else:
    print("not an odd minute.")