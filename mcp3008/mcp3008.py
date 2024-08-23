from datetime import datetime
import gpiozero as zero
import paho.mqtt.publish as publish
from dotenv import load_dotenv
import os
from time import sleep
load_dotenv()

def pass_data(light:float,potentiometer:float):
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now_str)
    message1 = f'''{{
        "value":{light},
        "date":"{now_str}",
        "topic":"501教室/光敏電阻"
    }}'''

    message2 = f'''{{
        "valuel":{potentiometer},
        "date":"{now_str}",
        "topic":"501教室/可變電阻"
    }}'''

    #要加入username和password
    publish.single(topic='501教室/光敏電阻',payload=message1,hostname='127.0.0.1',qos=2,auth={'password':os.environ['MQTT_PASSWORD'],'username':os.environ['MQTT_USERNAME']})
    publish.single(topic='501教室/可變電阻',payload=message2,hostname='127.0.0.1',qos=2,auth={'password':os.environ['MQTT_PASSWORD'],'username':os.environ['MQTT_USERNAME']})

if __name__ == '__main__':
    mcp3008_7 = zero.MCP3008(7);
    mcp3008_6 = zero.MCP3008(6);
    while True:
        print("the channel 7 光敏電阻:{:.2f}".format(mcp3008_7.value));
        print("the channel 6 可變電阻:{:.2f}".format(mcp3008_6.value))
        pass_data(light=mcp3008_7.value,potentiometer=mcp3008_6.value)
        sleep(1)