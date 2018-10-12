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

data_path = '/dataDir/'
zip_path = '/zipfile/'

def main():

    print("-- start --")

    while(cap.isOpened()):

        # VideoCaptureから1フレーム読み込む
        ret, frame = cap.read()

        # 1分おきに画像取得
        time.sleep(60)

        # 現在時刻の取得
        now = datetime.now()

        # "0915"のように，現在の日付を文字列で取得
        nowStr = now.strftime("%m%d")

        # "0915140532" のように、現在時刻を文字列で取得(画像の名前用)
        writeStr = now.strftime('%m%d%H%M%S')

        # 画像があるディレクトリ一覧
        datalist = os.listdir(data_path)

        for dataDate in datalist:
            if nowStr == dataDate:

                # 保存先ディレクトリのPATH
                saveDir = os.path.join(data_path, nowStr)

                # 保存用ファイル名
                saveImg = saveDir + '/' + writeStr

                # ./dataDir/0915 ディレクトリに取得画像を保存
                cv2.imwrite(saveImg +  ".png", frame)

                print(writeStr + ".png")

    # キャプチャをリリースして、ウィンドウをすべて閉じる
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
