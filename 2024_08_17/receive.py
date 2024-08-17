import paho.mqtt.client as mqtt

def on_message(mosq, obj, msg):
    topic = msg.topic
    message = msg.payload.decode('utf-8')
    print(f"topic={topic},message:{message}")

if __name__ == '__main__':
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect('127.0.0.1')
    client.subscribe('501教室/老師桌燈',qos=2)
    client.loop_forever()

