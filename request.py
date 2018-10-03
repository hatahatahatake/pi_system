#!/usr/bin/python3
# -*- coding: utf-8 -*-

# mac側で叩くコマンド用プログラム
# 圧縮ファイルをリクエストして解凍・保存する

import os
import sys
import glob
import shutil

def main():

    # zip ファイルを解凍
    sys.path.append('/Desktop/workspace/pi_server/flask_test')
    zip_path = './cap_images/' + '/*.zip'
    zip_file_list = glob.glob(path)
    print('zip file list:', zip_file_list)


    # 保存先をドライブに指定する



if __name__ == "__main__":
    main()
