# Program to block a list of website till a specific time
# Sarveshwar Shukla (19 March 2022)

import datetime 
import time

website_list = ["www.website1.com", "www.website2.com"]
block_the_website_till = datetime.datetime(2022,12,14)
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now()<block_the_website_till:
        print("Blocking Started")
        with open(host_path, "r+") as host_file:
            content = host_file.read()
            for website in website_list:
                if website not in content:
                    host_file.write(redirect + " " + website + "\n")
                else:
                    pass

    else:
        with open(host_path, "r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any( website in lines for website in website_list):
                    host_file.write(lines)

            host_file.truncate()   
        time.sleep(5)
            
