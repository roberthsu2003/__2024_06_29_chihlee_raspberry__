import signal
from gpiozero import Button,LED

def user_release():
    print("使用者按下放開")
    led.toggle()
    if led.is_lit:
        print("燈是開的")
    else:
        print("燈是關的")

if __name__ == '__main__':
    button = Button(pin=18)
    button.when_released = user_release
    led = LED(pin=25) 
    signal.pause()