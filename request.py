#!/usr/bin/python3
# -*- coding: utf-8 -*-

# mac側で叩くコマンド用プログラム
# 圧縮ファイルをリクエストして解凍・保存する

import os
import sys
import glob
import requests
import zipfile

url = 'https://localhost/collect:3000/'

download_path = '/pi_zip/'
save_path = '/pi_image/'

def main():

    while True:

        ## zip ファイルをリクエストしてAPI呼び出す
        r_zip = requests.get(url, )

        # application/zip
        print(r_zip.headers['Content-Type'])

        # 1009.zip
        filename_zip = os.path.basename(url)
        print(filename_zip)

        # zipファイルの読み込み
        with open(download_path + filename_zip, 'r') as f:
            f.write(r_zip.content)
            file.readlines()

            return filename_zip

            ## zipファイルの展開・保存
            files = glob(os.path.join(download_path, '*.zip'))

            # 対象のzipファイルをディレクトリ指定して解凍
            for file in files:
                with ZipFile(file) as zf:
                    zf.extractall(save_path)

if __name__ == "__main__":
    main()
