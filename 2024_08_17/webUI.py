import streamlit as st
import redis
import os
import json
from dotenv import load_dotenv
import pandas as pd
from streamlit_autorefresh import st_autorefresh

load_dotenv()
st_autorefresh()
conn = redis.Redis(host=os.environ['REDIS_HOST'],port=6379,password=os.environ['REDIS_PASSWORD'])
print(conn.ping())
bytes_list = conn.lrange('501教室/老師桌燈',-5,-1)
str_list = [bytes_str.decode('utf-8') for bytes_str in reversed(bytes_list)]
dict_list = [json.loads(string) for string in str_list]
df1 = pd.DataFrame(dict_list)
df1

