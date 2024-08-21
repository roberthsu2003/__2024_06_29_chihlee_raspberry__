import streamlit as st
import redis
import os
import json
from dotenv import load_dotenv
import pandas as pd
from streamlit_autorefresh import st_autorefresh

load_dotenv()
st_autorefresh()
#conn = redis.Redis(host=os.environ['REDIS_HOST'],port=6379,password=os.environ['REDIS_PASSWORD'])
conn = redis.Redis.from_url(url=os.environ['RENDER_REDIS_INTERNAL'])
bytes_list = conn.lrange('501教室/老師桌燈',-5,-1) #取得的資料為list內有bytes string
str_list = [bytes_str.decode('utf-8') for bytes_str in reversed(bytes_list)] #將bytes string轉換為str
dict_list = [json.loads(string) for string in str_list] #將字串轉為python的資料結構
df1 = pd.DataFrame(dict_list) #建立DataFrame
st.title("訓練通教室")
st.header("感測器:blue[cool] :sunglasses:")
st.dataframe(df1,
             hide_index=True,
             column_config={
                 "status":st.column_config.CheckboxColumn(label='按鈕狀態',width='small'),
                 "date":st.column_config.DatetimeColumn(label='時間',width='medium')
                 })


