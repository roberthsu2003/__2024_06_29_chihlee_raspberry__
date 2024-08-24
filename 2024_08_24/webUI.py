import streamlit as st
import redis
from dotenv import load_dotenv
import os
import json

load_dotenv()
redis_conn = redis.Redis(host=os.environ['REDIS_HOST'], port=6379,password=os.environ['REDIS_PASSWORD'])
bytes_list = redis_conn.lrange('501教室/老師桌燈',-10,-5)
#將bytes string 轉換為str
str_list = [bytes_str.decode('utf-8') for bytes_str in bytes_list]

dict_list = [json.loads(string) for string in str_list]
st.write(dict_list)

st.title("訓練通教室")
st.header("感測器:blue[cool] :sunglasses:")