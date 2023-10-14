# 導入必要的模組
import serial
import struct
import datetime
import json
import time
from mmWave import peopleMB
##v6.py作用:只會產生一次v6當前點的數據
'''
v6: point cloud 2d infomation
v7: Target Object information
v8: Target Index information
v6格式range:float #Range, in m
azimuth:float	#Angle, in rad
doppler:float	#Doppler, in m/s
snr:float #SNR, ratio
ex:(range,azimuth,doppler,snr)
定義全局變量類
'''
class globalV:
    count = 0
    def __init__(self, count):
        self.count = count

# 開啟串行端口
port = serial.Serial("/dev/ttyS0",baudrate = 921600, timeout = 0.5)

# 創建全局變量和peopleMB對象
gv = globalV(0)
pm = peopleMB.PeopleMB(port)


# Use the tlvRead method to get the data
# The argument 'disp' determines whether to display debug information.
# Set it to True if you want to see debug information.
# The method returns a tuple with data availability flag, v6 data, v7 data, and v8 data.
data_available, v6, v7, v8 = pm.tlvRead(disp=True)
#disp=False 可以不詳細顯示出其他數據

# Check if data is available
if data_available:
    # Process v6 data
    print("v6 data:")
    for item in v6:
        print(item,end=',')
else:
    print("No data available.")





