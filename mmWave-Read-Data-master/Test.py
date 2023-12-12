import json
import os
import re
import time
import imageio
import shutil

import matplotlib.pyplot as plt


def images_to_mp4(image_folder, output_file):
    images = []
    for file_name in sorted(os.listdir(image_folder)):
        if file_name.endswith('.png'):
            file_path = os.path.join(image_folder, file_name)
            images.append(imageio.imread(file_path))
    imageio.mimsave(output_file, images, fps=11)  # fps 是每秒的幀數


def read_and_save_as_json(file_name):
    # 刪除 'images' 資料夾中的所有圖片
    for file_name in os.listdir('images'):
        file_path = os.path.join('images', file_name)
        os.remove(file_path)

    with open(file_name, 'r') as file:
        for i, line in enumerate(file):
            line_data = json.loads(line)

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            # 提取 x, y, 和 z 座標
            x = [point[0] for point in line_data]
            y = [point[1] for point in line_data]
            z = [point[2] for point in line_data]

            # 繪製點雲圖
            ax.scatter(x, z, y)
            ax.set_xlim(-5, 5)
            ax.set_ylim(-5, 5)
            ax.set_zlim(0, 4)

            # 儲存圖片
            if not os.path.exists('images'):
                os.makedirs('images')
            plt.savefig(f'images/figure_{i}.png')
            plt.close(fig)
            print(f"現在進度: {i}")

shutil.rmtree("images")
os.mkdir("images")

# 呼叫函式
read_and_save_as_json(r'/home/led/mmwave-project/mmwave/mmWave-Read-Data-master/static/data/20231212-145129.json')


time.sleep(2)
images_to_mp4('images', 'output.mp4')
