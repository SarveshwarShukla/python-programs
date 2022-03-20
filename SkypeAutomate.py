# Program to automate skype 
# Sarveshwar Shukla (20 March 2022)

from skpy import Skype
import os.path

user_email = "hello@world.com"
user_password = "hello_password"

user_info = Skype(user_email, user_password)

# storing contact info of all the contacts in a list
contacts_info = user_info.contacts

# sends message to the user (the live id can be obtained from the above list using for loop)
send_message = user_info.contacts["live id of the reciver"].chat.sendMsg("Welcome")

# sending group message to two or more contacts (ie creating a group)
group_message = user_info.chats.create(["live id1", "live id2", "etc.."])

# sending images
with open("path ie C:/Users/Desktop../test.png", "rb") as f:
    user_info.contacts["live id1"].chat.sendFile(f, "test.png", image=True)

