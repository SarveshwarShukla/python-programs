# CAREFUL (any unsaved work will be lost due to restart or shutdown)

# Program to Restart, Logout and Shutdown the Computer upon click
# can be further modified to do this on passing some command into the powershell
# Sarveshwar Shukla (17 March 2022)

from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 60")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")



shutDownApplication = Tk()
shutDownApplication.title("ShutDown App")
shutDownApplication.geometry("500x500")
shutDownApplication.config(bg="#000E35")

restartButton = Button(shutDownApplication, text="Restart", font=(
    "Time New Roman", 12, "bold"), relief=RAISED,command=restart)
restartButton.place(x=35, y=60, height=50, width=200)

restartWithTimeButton = Button(shutDownApplication, text="Restart (1min)", font=(
    "Time New Roman", 12, "bold"), relief=RAISED,command=restart_time)
restartWithTimeButton.place(x=265, y=60, height=50, width=200)

logoutButton =  Button(shutDownApplication, text="Log Out", font=(
    "Time New Roman", 12, "bold"), relief=RAISED,command=logout)
logoutButton.place(x=35, y=150, height=50, width=200)

shutDownButton =  Button(shutDownApplication, text="Shut Down", font=(
    "Time New Roman", 12, "bold"), relief=RAISED,command=shutdown)
shutDownButton.place(x=265, y=150, height=50, width=200)


shutDownApplication.mainloop()
