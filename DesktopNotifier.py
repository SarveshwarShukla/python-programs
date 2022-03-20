# Creating a desktop notifier to take rest
# Sarveshwar Shukla (19 March 2022)

from socket import timeout
from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(title=" TAKE REST ", message="Timed rest is also important while working", app_icon="./assets/test.ico", timeout=5)
        time.sleep(3600) # 3600 seconds = 1hour