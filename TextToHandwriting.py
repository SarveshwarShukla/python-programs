# Program to convert the passed text into handwriting
# Sarveshwar Shukla (19 March 2022)

# When the string is passed manually using triple quotes then it recognises the new line, but when taking user input, it only records till enter is pressed, needs modification (using loop)

import pywhatkit as pw

# text = """What are you doing, 
# is this apple""" # manual input

text = input("Enter the text : ")
print("Converting the entered text into handwriting, please wait ")

handwritingColor = [0,14,53]

pw.text_to_handwriting(text, "demo.png", handwritingColor)
print("Completed!")