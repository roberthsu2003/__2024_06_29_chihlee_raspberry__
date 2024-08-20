#!/bin/bash
#進入腳本所有目錄
cd "$(dirname "$0")"

#進入venv1
source ~/miniforge3/etc/profile.d/conda.sh
conda activate venv1

#執行python程式,一次啟動3個,必需要有&連結
python button1.py &
python receive.py &
streamlit run webUI.py &