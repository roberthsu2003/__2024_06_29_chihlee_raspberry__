#!/bin/bash
#進入腳本所有目錄
cd "$(dirname "$0")"

#進入venv1
conda activate venv1

#執行python程式
python button1.py
python receive.py
streamlit run webUI.py