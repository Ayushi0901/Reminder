import time
from plyer import notification

if __name__== "__main__":
    while True :
        notification.notify(
            title="Please go and do CODE",
            message="Coding will given you great job..........",
            app_icon="image\icon.ico",
            timeout=10
        
    )
    time.sleep(60*60)