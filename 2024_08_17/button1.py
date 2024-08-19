import signal
from gpiozero import Button,LED
from datetime import datetime
import paho.mqtt.publish as publish
from dotenv import load_dotenv
import os
load_dotenv()

def user_release():
    print("使用者按下放開")
    led.toggle()
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now_str)
    if led.is_lit:
        message = f'''{{
            "status":"true",
            "date":"{now_str}",
            "topic":"501教室/老師桌燈"
        }}'''
        print(message)
        #要加入username和password
        publish.single(topic='501教室/老師桌燈',payload=message,hostname='127.0.0.1',qos=2,auth={'password':os.environ['MQTT_PASSWORD'],'username':os.environ['MQTT_USERNAME']})
    else:
        message = f'''{{
            "status":"false",
            "date":"{now_str}",
            "topic":"501教室/老師桌燈"
        }}''' 
        print(message)
        publish.single(topic='501教室/老師桌燈',payload=message,hostname='127.0.0.1',qos=2,auth={'password':os.environ['MQTT_PASSWORD'],'username':os.environ['MQTT_USERNAME']})

if __name__ == '__main__':
    button = Button(pin=18)
    button.when_released = user_release
    led = LED(pin=25) 
    signal.pause()