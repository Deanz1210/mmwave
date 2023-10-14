import json
import serial
import struct
import datetime
import time
import os
from mmWave import peopleMB

class globalV:
    count = 0
    def __init__(self, count):
        self.count = count

port = serial.Serial("/dev/ttyS0",baudrate = 921600, timeout = 0.5)

gv = globalV(0)
pm = peopleMB.PeopleMB(port)

collecting_data = True  # 添加一個標誌變量來控制數據采集


try:
    count = 0
    while collecting_data:
        data_available, v6, v7, v8 = pm.tlvRead(disp=True)
        if data_available:
            print("v6 data:")
            for item in v6:
                print(item,end=',')
                
            # 將v6、v7和v8資料轉換為JSON格式
            data_json = json.dumps({"v6": v6, "v7": v7, "v8": v8})
            
            # 儲存JSON格式的資料
            with open('data.json', 'w') as json_file:
                json_file.write(data_json)
        else:
            print("No data available.")
        
        count += 1
        if count >= 10:  # 假設你想在100次迭代後停止
            print("\n到達自定義暫停點")
            collecting_data = False
                
except KeyboardInterrupt:  # 當按下 Ctrl + C 時觸發 KeyboardInterrupt 異常
    print("\n停止數據采集")
    collecting_data = False
