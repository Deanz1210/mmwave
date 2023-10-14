import json
import serial
import struct
import datetime
import time
from mmWave import peopleMB
import os

class globalV:
    count = 0
    def __init__(self, count):
        self.count = count

port = serial.Serial("/dev/ttyS0",baudrate = 921600, timeout = 0.5)

gv = globalV(0)
pm = peopleMB.PeopleMB(port)

# 檢查目錄是否存在，如果不存在則建立它
directory = '/home/led/mmwave-project/mmWave/TEST/TestLED/v678data/'
os.makedirs(directory, exist_ok=True)

collecting_data = True  # 添加一個標誌變量來控制數據采集


# 初始化一個字典來儲存v6、v7和v8的數據
data_dict = {"v6": [], "v7": [], "v8": []}

try:
    count = 0
    while collecting_data:
        data_available, v6, v7, v8 = pm.tlvRead(disp=True)
        if data_available:
            print("v6 data:")
            for item in v6:
                print(item,end=',')
                
            # 將v6、v7和v8的數據添加到字典中
            data_dict["v6"].extend(v6)
            data_dict["v7"].extend(v7)
            data_dict["v8"].extend(v8)
        
        count += 1
        if count >= 2:  # 假設你想在10次迭代後停止
            print("\n到達自定義暫停點")
            collecting_data = False
                
except KeyboardInterrupt:  # 當按下 Ctrl + C 時觸發 KeyboardInterrupt 異常
    print("\n停止數據采集")
    collecting_data = False

# 將字典轉換為JSON格式
data_json = json.dumps(data_dict)

# 取得當前時間並轉換為字串格式
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# 儲存JSON格式的資料，檔名包含時間戳，並儲存在指定的資料夾
with open(f'/home/led/mmwave-project/mmWave/TEST/TestLED/v678data/data_{timestamp}.json', 'w') as json_file:
    json_file.write(data_json)
