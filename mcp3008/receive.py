from time import sleep
import paho.mqtt.client as mqtt
import redis
from dotenv import load_dotenv
import os
#from tools.file import created_log_file,record_info
import json
from datetime import datetime
import threading

#MQTT接收訊息的callback
def on_message(mosq, obj, msg):
    topic = msg.topico
    print(topic)
    '''
    message = msg.payload.decode('utf-8')#預設是binary str,轉換為str
    redis_conn.rpush(topic,message) #儲存在本機端redis
    #render_redis_conn.rpush(topic,message)#儲存在render server的redis
    #解析json文字檔
    message_dict = json.loads(message)
    print(message)
    #儲存檔案
    now = datetime.now()
    current_file_name = now.strftime('%Y_%m_%d.log')
    log_path = created_log_file(current_file_name)
    record_info(log_path,message_dict['topic'],message_dict['date'],str(message_dict['status']))
    print(f"topic={topic},message:{message}")
    '''
def mqtt_thread(client):
    client.loop_forever()
    
if __name__ == "__main__":
    load_dotenv()
    redis_conn = redis.Redis(host=os.environ['REDIS_HOST'], port=6379,password=os.environ['REDIS_PASSWORD'])
    #MQTT建立subscribe
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(os.environ['MQTT_USERNAME'],os.environ['MQTT_PASSWORD']) #加入username和password
    client.on_message = on_message
    client.connect(os.environ['MQTT_SERVER'])
    client.subscribe('501教室/光敏電阻',qos=2)
    client.subscribe('501教室/可變電阻',qos=2)
    #將mqtt的執行使用其它執行緒來負責
    thread = threading.Thread(target=mqtt_thread,kwargs={'client':client})
    thread.start()
    try:
        while True:
            #sleep()不會影響其它的執行緒
            sleep(1)
    except KeyboardInterrupt:
        print("MQTT 停止連線")
        client.disconnect()
        thread.join()
        print("MQTT client stopped.")

