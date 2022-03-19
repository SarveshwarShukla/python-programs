# Program to generate QR Code of a String given by user
# Sarveshwar Shukla (17 March 2022)

# Method 1 (not working)
# import qrcode as qr
# qrcodeimage = qr.make("https://sarveshwarshukla.com")
# qrcodeimage.save("sarveshwarshukla.png")


# Method 2 (working)
import pyqrcode
import png
from pyqrcode import QRCode

# inputGiven = "https://sarveshwarshukla.com" # program input
inputGiven = input("Enter the string of which you want to create QR code of")  # manual input
codeColor = "#1B3B92"
backgroundColor = "#FFFFFF"

QRCodeGenerated = pyqrcode.create(inputGiven)
QRCodeGenerated.svg("QR.svg", scale=8,module_color=codeColor, background=backgroundColor)
# QRCodeGenerated.png("QR.png", scale=100) # more we increase the sclae, more the size will become
QRCodeGenerated.png("QR.png", scale=6,module_color=codeColor, background=backgroundColor)
