#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 前画像と差分を求めるプログラム 12/13~

import cv2
import os
import sys
import glob
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from pathlib import Path

#data_path = '/home/pi/Desktop/pi_system/raspi/dataDir/'
data_path = '/Users/yuka/Desktop/resarch/pi_system/raspi/dataDir/'
output_path = '/Users/yuka/Desktop/resarch/pi_system/raspi/diffDir/'

if __name__ == '__main__':

    while True:

        print("-- start --")

        # 画像があるディレクトリ一覧
        datalist = os.listdir(data_path)

        # img を格納
        img = []
        all_img = []

        for dataDate in datalist:
        #    if dataDate.endswith(".png"):

            print("-- search pngdata --")

            #
            print(dataDate)

            pathStr = str(dataDate)
            img = np.array(dataDate)
            img = cv2.imread(pathStr)
            print(img)

            all_img.append(img)
            print(all_img)

            for dataDate in range(len(datalist)):


                print("-- create diff image --")

                #img = img[0]
                img = cv2.imread(pathStr)

                cv2.imshow(diff_img, frame)


                cv2.imwrite(output_path + dataDate, frame)

                print(diff_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# return all_img
