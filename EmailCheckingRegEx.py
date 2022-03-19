# Program to check if an entered email is valid or not using regex (regular expressions)
# Sarveshwar Shukla (17 March 2022)

# Not very effective, needs modifications
import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter the Email : ")

if re.search(email_condition, user_email):
    print("Email is valid")
else:
    print("Email is invalid")