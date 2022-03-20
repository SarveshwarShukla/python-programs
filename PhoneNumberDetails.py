# Program to find high level details of a phone number
# Sarveshwar Shukla (19 March 2022)

import phonenumbers
from phonenumbers import timezone, geocoder, carrier

numberInput = input("Enter the Phone Number with country code: ")
numberInfo = phonenumbers.parse(numberInput)
timeZoneInfo = timezone.time_zones_for_number(numberInfo)
carrierInfo = carrier.name_for_number(numberInfo, "en")
locationInfo = geocoder.description_for_number(numberInfo, "en")

print(numberInfo)
print(timeZoneInfo)
print(carrierInfo)
print(locationInfo)