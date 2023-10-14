import json
import serial
import struct
import datetime
import time
from mmWave import peopleMB

class globalV:
    count = 0
    def __init__(self, count):
        self.count = count

port = serial.Serial("/dev/ttyS0",baudrate = 921600, timeout = 0.5)

gv = globalV(0)
pm = peopleMB.PeopleMB(port)

data_available, v6, v7, v8 = pm.tlvRead(disp=True)

ollecting_data = True  # 添加一个标志变量来控制数据采集

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
