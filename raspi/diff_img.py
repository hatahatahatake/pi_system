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

data_path = '/Users/yuka/Desktop/resarch/pi_system/raspi/dataDir/'
output_path = '/Users/yuka/Desktop/resarch/pi_system/raspi/diffDir/'
jpgDiff_path = '/Users/yuka/Desktop/resarch/pi_system/raspi/jpgDiff/'

# データリストファイル
list_path = '/Users/yuka/Desktop/resarch/pi_system/raspi/img_data.txt'

if __name__ == '__main__':

    while True:

        print("-- start --")

        # 画像があるディレクトリ一覧
        datalist1 = os.listdir(data_path)
        datalist1.sort()

        datalist2 = datalist1
        datalist2.sort()


        for i, dataDate in enumerate(datalist1):

            count = 0

            #拡張子なしでファイル名の取得
            filename, ext = os.path.splitext(dataDate)

            print("-- create diffdata --")

            dataDate = os.path.join(data_path, dataDate)
            dataDate2 = os.path.join(data_path, datalist2[i+1])
            dataDate1 = cv2.imread(dataDate)
            dataDate2 = cv2.imread(dataDate2)

            # 画像間差分を計算
            dataDate3 = dataDate2 - dataDate1

            # どこまでできているか
            count += i
            print(count)

            #print(dataDate3)

            # 絶対値の計算
            #dataDate3 = abs(dataDate3)

            # ピクセルにマイナス値があれば0とする
            for q in range(dataDate3.shape[0]):
                for r in range(dataDate3.shape[1]):
                    for s in range(dataDate3.shape[2]):
                        count = []
                        sub = dataDate3[q,r,s]
                        if sub < 0:
                            dataDate3[q,r,s] = 0

            # 差分をグレースケール化する
            dataDate3 = cv2.cvtColor(dataDate3, cv2.COLOR_BGR2GRAY)

            # 差分画像を表示
            cv2.imshow('diff Image', dataDate3)

            # png で保存
            saveDiff = output_path + "diff_" + filename
            saveImg = cv2.imwrite(saveDiff + ".png", dataDate3)
            saveImg.sort()
            print("diff_" + filename + ".png")

            # png sub
            #subDiff = output_path + "diff_" + filename
            #cv2.imwrite(saveDiff + ".png", dataDate4)
            #print("subDiff_" + filename + ".png")

            # jpg で保存
            saveDiff2 = jpgDiff_path + "diff_" + filename
            saveImg2 = cv2.imwrite(saveDiff2 + ".jpg", dataDate3)
            saveImg2.sort()
            print("diff_"  + filename + ".jpg")
