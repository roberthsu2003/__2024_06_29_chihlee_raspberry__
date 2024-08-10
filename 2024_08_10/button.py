from gpiozero import Button

button = Button(pin=)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")