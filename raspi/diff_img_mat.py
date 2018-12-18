#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 前画像と差分を求めるプログラム 12/13~
#https://algorithm.joho.info/programming/python/opencv-frame-difference-py/

import cv2
import numpy as np

input_path = '/Users/yuka/Desktop/pi_system/resarch/raspi/dataDir/'
output_path = '/Users/yuka/Desktop/resarch/pi_system/raspi/jpg_data/'

# フレーム差分の計算
def main():

    while():

        img1 = input_path + '/181114000705.png'    # 115KB
        img2 = input_path + '/181113174034.png'    # 239KB
        img3 = input_path + '/181114130941.png'    # 435KB

        # フレームの絶対差分
        diff1 = cv2.absdiff(img1, img2)
        diff2 = cv2.absdiff(img2, img3)

        # 2つの差分画像の論理積
        diff = cv2.bitwise_and(diff1, diff2)

        # 二値化処理
        diff[diff < th] = 0
        diff[diff >= th] = 255

        # メディアンフィルタ処理（ゴマ塩ノイズ除去）
        mask = cv2.medianBlur(diff, 3)

        return  mask

    #cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
