import serial
import math
import struct
import datetime
import json
import time
import threading
import sys
from mmWave import peopleMB


# 定義一個全局變量類
class globalV:
    count = 0

    def __init__(self, count):
        self.count = count


# 創建一個變數來標識是否停止程式
stop_program = False


# 函數，用於處理鍵盤輸入
def keyboard_input():
    global stop_program
    while True:
        command = input("輸入 'stop' 以停止程式: ")
        if command.lower() == "stop":
            stop_program = True
            break


# 開啟串行端口
port = serial.Serial("/dev/ttyS0", baudrate=921600, timeout=0.5)

# 創建全局變量和peopleMB對象
gv = globalV(0)
pm = peopleMB.PeopleMB(port)

# 啟動鍵盤輸入處理的獨立線程
keyboard_thread = threading.Thread(target=keyboard_input)
keyboard_thread.start()

while not stop_program:
    # Use the tlvRead method to get the data
    data_available, v6, v7, v8 = pm.tlvRead(disp=False)
    # disp=False 可以不詳細顯示出其他數據
    if data_available:
        # Process v6 data
        print()
        print("v6 data:")
        for i, item in enumerate(v6):
            range, azimuth = item[0], item[1]
            print(f'({range}, {azimuth})', end='')
            if i < len(v6) - 1:
                print(',', end='')
    
        print()  # 打印一个空行
        print("x,y轉換:")
        for i, item in enumerate(v6):
            range, azimuth = item[0], item[1]
            x = range * math.cos(azimuth)
            y = range * math.sin(azimuth)   
            print(f'({x}, {y})', end='')
            if i < len(v6) - 1:
                print(',', end='')
        
    else:
        print("No data available.")

    time.sleep(1)  # 控制數據獲取速率

# 程式結束
print("程式已停止。")
