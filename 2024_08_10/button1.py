import signal
from gpiozero import Button

def user_release():
    print("使用者按下放開")

if __name__ == '__main__':
    button = Button(pin=18)
    button.when_released = user_release 
    
    signal.pause()