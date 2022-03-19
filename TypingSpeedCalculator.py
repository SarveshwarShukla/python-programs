# Program to check typing speed 
# can be modified, not in best form
# Sarveshwar Shukla (17 March 2022)

from asyncore import read
from time import *
import random as r

from pymysql import Timestamp

def mistake(paragraphText, userInput):
    error = 0
    for i in range(len(paragraphText)):
        try:
            if paragraphText[i] == userInput[i]:
                pass
            else:
                error +=1
        except:
            error = error + 1
    return error
    
def speed_time(time_start, time_end,userInput):
    time_delay = time_end - time_start
    time_roundoff = round(time_delay,2)
    speed = len(userInput)/time_roundoff
    return round(speed)
    


paragraphText = ["lorem ipsum dolar sit hello world is a good boy", "what is your name bro", "hello bro what is your name"]
paragraphTextSelection = r.choice(paragraphText)
print("Typing Speed Calculator=====")
readyVar = input("Ready to test Yes / No : ")
if readyVar.lower() == "yes":
    print()
    print(paragraphTextSelection)
    print()
    time_start = time()
    userInput = input("Start Typing : ")
    time_end = time()

    print("Speed : ", speed_time(time_start, time_end, userInput), " w/seconds")
    print("Errors : ", mistake(paragraphTextSelection, userInput))
elif readyVar.lower() == "no":
    print("Thank You")
    print()
else:
    print("Please type between Yes and No")
    print()