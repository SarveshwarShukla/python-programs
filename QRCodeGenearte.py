# import qrcode as qr
# image2 = qr.make("https://sarveshwarshukla.com")
# image2.save("sarveshwarshukla.png")

import pyqrcode
import png
from pyqrcode import QRCode

inputGiven = "https://sarveshwarshukla.com"
QRCodeGenerated = pyqrcode.create(inputGiven)
QRCodeGenerated.svg("QR.svg", scale=8)
# QRCodeGenerated.png("QR.png", scale=100) # more we increase the sclae, more the size will become
QRCodeGenerated.png("QR.png", scale=6)
