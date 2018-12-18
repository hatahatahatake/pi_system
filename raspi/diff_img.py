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
jpgDiff_path = '/Users/yuka/Desktop/resarch/pi_system/raspi/jpgDiff/'

if __name__ == '__main__':

    while True:

        print("-- start --")

        # 画像があるディレクトリ一覧
        datalist1 = os.listdir(data_path)
        datalist2 = datalist1

        for i, dataDate in enumerate(datalist1):

            print("-- create diffdata --")

            # 拡張子なしでファイル名の取得
            filename, ext = os.path.splitext(dataDate)

            dataDate = os.path.join(data_path, dataDate)
            dataDate2 = os.path.join(data_path, datalist2[i+1])
            dataDate1 = cv2.imread(dataDate)
            dataDate2 = cv2.imread(dataDate2)

            # 画像間差分を計算
            dataDate3 = dataDate2 - dataDate1

            # 差分画像を表示
            cv2.imshow('diff Image', dataDate3)

            # png で保存
            saveDiff = output_path + filename
            cv2.imwrite(saveDiff + ".png", dataDate3)
            print(filename + ".png")

            # jpg で保存
            saveDiff2 = jpgDiff_path + filename
            save2 = cv2.imwrite(saveDiff2 + ".jpg", dataDate3)
            print(filename + ".jpg")
