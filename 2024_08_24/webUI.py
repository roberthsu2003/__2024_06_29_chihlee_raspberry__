import streamlit as st
import redis
from dotenv import load_dotenv
import os
import json
import pandas as pd
from streamlit_autorefresh import st_autorefresh

load_dotenv()
st_autorefresh()
redis_conn = redis.Redis(host=os.environ['REDIS_HOST'], port=6379,password=os.environ['REDIS_PASSWORD'])
bytes_list = redis_conn.lrange('501教室/老師桌燈',-5,-1)
#將bytes string 轉換為str
str_list = [bytes_str.decode('utf-8') for bytes_str in reversed(bytes_list)]

dict_list = [json.loads(string) for string in str_list]
df1 = pd.DataFrame(dict_list)

st.title("訓練通教室")
st.header("感測器:blue[cool] :sunglasses:")
st.dataframe(df1,
             hide_index=True,
             column_config={
                 "status":st.column_config.CheckboxColumn(label='按鈕狀態',width='small'),
                 "date":st.column_config.DatetimeColumn(label='時間',width='medium')
             })