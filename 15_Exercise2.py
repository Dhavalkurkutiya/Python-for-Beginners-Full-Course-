# Excersice 2: Good Morning
import time
import datetime


CURRENT_TIME = datetime.datetime.now()
CURRENT_TIME = CURRENT_TIME.strftime("%H:%M:%S")
CURRENT_TIME = CURRENT_TIME + " PM"


if CURRENT_TIME >= "00:00:00 PM" and CURRENT_TIME < "12:00:00 PM":
    print("Good Morning")
elif CURRENT_TIME >= "12:00:00 PM" and CURRENT_TIME < "06:00:00 PM":
    print("Good Afternoon")
elif CURRENT_TIME >= "06:00:00 PM" and CURRENT_TIME < "09:00:00 PM":
    print("Good Evening")
else:
    print("Good Night")

    
print(CURRENT_TIME)