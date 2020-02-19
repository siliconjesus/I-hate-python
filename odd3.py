from datetime import datetime
# Extension of previous - do everything at one time - eliminate the need for the extra variable.
# again - probably breaks some python simplicity guide.
if (datetime.today().minute % 2):
    print("this minute seems a little odd.")
else:
    print("not an odd minute.")