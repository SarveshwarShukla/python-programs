# Program to Automate Gmail
# Sarveshwar Shukla (20 March 2022)

import smtplib as s


gmail_username = "hello@gmail.com"
gmail_password = "hello_password"

smtp_object = s.SMTP("smtp.gmail.com", 587)
smtp_object.ehlo()
smtp_object.starttls()
smtp_object.login(gmail_username, gmail_password)
subject = "Testing Subject"
body = "Testing Description"
message = f"subject:{subject}\n\n{body}"
listMailAddress = ["hello1@gmail.com", "hello2@gmail.com"]

smtp_object.sendmail(gmail_username, listMailAddress, message)
print("Mail Sent")
smtp_object.quit()