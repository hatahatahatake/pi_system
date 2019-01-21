#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Webカメラ 画像取得コード　9/19 完成
# raspberryPi3 コンパイル用
# 写真を撮り続けて0時になったら新ディレクトリに保存可能

import cv2
import os
import sys
import time
import datetime

from threading import Timer
from time import sleep
from datetime import datetime, timedelta

# VideoCaptureのインスタンスを作成する。
# 0は内蔵カメラ、1は入力カメラ
cap = cv2.VideoCapture(0)
cap.set(4, 800)  # Width
cap.set(4, 600)  # Heigh
cap.set(5, 15)   # FPS

data_path = '/home/pi/Desktop/pi_system/raspi/dataDir/'
jpg_path = '/home/pi/Desktop/pi_system/raspi/jpgDir/'

#ata_path = '/Users/yuka/Desktop/resarch/pi_system/raspi/dataDir/'
#jpg_path = '/Users/yuka/Desktop/resarch/pi_system/raspi/jpgDir/'

#pass2 = '/Users/yuka/Desktop/resarch/pi_system/raspi/kutiot1.pem'

def main():

    print("-- start --")

    while(cap.isOpened()):

        # VideoCaptureから1フレーム読み込む
        ret, frame = cap.read()

        # 1分おきに画像取得
        time.sleep(180)

        # 現在時刻の取得
        now = datetime.now()

        # "20180915140532" のように、現在時刻を文字列で取得(画像の名前用)
        writeStr = now.strftime('%y%m%d%H%M%S')

        # png ディレクトリに取得画像を保存
        saveImg = data_path + writeStr
        png_save = cv2.imwrite(saveImg + ".png", frame)
        print('scp ' + png_save + ' ubuntu@18.179.34.84:/home/ubuntu/Desktop/hatapic/' + writeStr + '.png')
        os.system('scp ' +  "-i " + png_save + ' ubuntu@18.179.34.84:/home/ubuntu/Desktop/hatapic/' + writeStr + ".png")

        # jpg ディレクトリに取得画像を保存
        saveImg2 = jpg_path + writeStr
        jpg_save = cv2.imwrite(saveImg2 + ".jpg", frame)
        print('scp ' + jpg_save + ' ubuntu@18.179.34.84:/home/ubuntu/Desktop/hatapic/' + writeStr + '.jpg')
        os.system('scp ' + "-i " + jpg_save + ' ubuntu@18.179.34.84:/home/ubuntu/Desktop/hatapic/' + writeStr + ".jpg")

    # キャプチャをリリースして、ウィンドウをすべて閉じる
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
