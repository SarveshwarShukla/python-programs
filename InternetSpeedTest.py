# Program to Measure Internet Speed (GUI)
# Sarveshwar Shukla (19 March 2022)

from tkinter import *
import speedtest

# def temporary():
#     lableInfo.config(text="Please wait for few seconds, speed is getting calculated")
#     speedCheck()
#     lableInfo.config(text="")

def speedCheck():
    lableSpeedTest_download.config(text="00")
    lableSpeedTest_upload.config(text="00")
    speedTestWindow = speedtest.Speedtest()
    speedTestWindow.get_servers()
    # will result in bit/second, we need to manually convert it to mb/s
    downloadSpeed = str(round(speedTestWindow.download()/(10**6), 3)) + " Mbps"
    uploadSpeed = str(round(speedTestWindow.upload()/(10**6), 3)) + " Mbps"
    lableSpeedTest_download.config(text=downloadSpeed)
    lableSpeedTest_upload.config(text=uploadSpeed)


speedTestWindow = Tk()
speedTestWindow.title("Internet Speed Test")
speedTestWindow.geometry("500x500")
speedTestWindowBackgroundColor = "#000E35"
speedTestWindowTextColor = "#FFFFFF"
speedTestWindow.config(bg=speedTestWindowBackgroundColor)

lableSpeedTest = Label(speedTestWindow, text="Internet Speed Test", font=(
    "Time New Roman", 20, "bold"), bg=speedTestWindowBackgroundColor, fg=speedTestWindowTextColor)
lableSpeedTest.place(x=40, y=40)

lableSpeedTest = Label(speedTestWindow, text="Download Speed", font=(
    "Time New Roman", 20, "bold"), bg=speedTestWindowBackgroundColor, fg=speedTestWindowTextColor)
lableSpeedTest.place(x=40, y=100)

lableSpeedTest_download = Label(speedTestWindow, text="00", font=(
    "Time New Roman", 20, "bold"), bg=speedTestWindowBackgroundColor, fg=speedTestWindowTextColor)
lableSpeedTest_download.place(x=300, y=100)

lableSpeedTest = Label(speedTestWindow, text="Upload Speed", font=(
    "Time New Roman", 20, "bold"), bg=speedTestWindowBackgroundColor, fg=speedTestWindowTextColor)
lableSpeedTest.place(x=40, y=160)

lableSpeedTest_upload = Label(speedTestWindow, text="00", font=(
    "Time New Roman", 20, "bold"), bg=speedTestWindowBackgroundColor, fg=speedTestWindowTextColor)
lableSpeedTest_upload.place(x=300, y=160)


button = Button(speedTestWindow, text="Check Speed", font=(
    "Time New Roman", 20, "bold"), relief=RAISED, command=speedCheck)
button.place(x=40, y=220)

lableInfo = Label(speedTestWindow, text="Please wait for few seconds after clicking on check speed", font=("Time New Roman", 10, "bold"), bg=speedTestWindowBackgroundColor, fg=speedTestWindowTextColor)
lableInfo.place(x = 40, y = 290)

speedTestWindow.mainloop()
