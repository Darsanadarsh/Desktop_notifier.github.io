from plyer import notification
import time
def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\user\\Downloads\\favicon (1).ico",
        timeout = 10,
    )
if __name__ == '__main__':
    while True:
        notifyMe("Heyy! Beware it's  corona time!👀😅",  "It's time to wash your hands 🖐️ \nDid you wore your mask? 😷 \nKeep social distance")
        time.sleep(1200)