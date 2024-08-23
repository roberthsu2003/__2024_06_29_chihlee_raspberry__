import paho.mqtt.client as mqtt
import redis
from dotenv import load_dotenv
import os
#from tools.file import created_log_file,record_info
import json
from datetime import datetime
load_dotenv()

redis_conn = redis.Redis(host=os.environ['REDIS_HOST'], port=6379,password=os.environ['REDIS_PASSWORD'])
render_redis_conn = redis.Redis.from_url(os.environ['RENDER_REDIS'])


#MQTT接收訊息的callback
def on_message(mosq, obj, msg):
    topic = msg.topic
    message = msg.payload.decode('utf-8')#預設是binary str,轉換為str
    redis_conn.rpush(topic,message) #儲存在本機端redis
    render_redis_conn.rpush(topic,message)#儲存在render server的redis
    #解析json文字檔
    message_dict = json.loads(message)
    print(message)
    #儲存檔案
    now = datetime.now()
    current_file_name = now.strftime('%Y_%m_%d.log')
    log_path = created_log_file(current_file_name)
    record_info(log_path,message_dict['topic'],message_dict['date'],str(message_dict['status']))


    print(f"topic={topic},message:{message}")

if __name__ == '__main__':
    #MQTT建立subscribe
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(os.environ['MQTT_USERNAME'],os.environ['MQTT_PASSWORD']) #加入username和password
    client.on_message = on_message
    client.connect(os.environ['MQTT_SERVER'])
    client.subscribe('501教室/老師桌燈',qos=2)
    client.loop_forever()

