#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Flask を使用した画像取得プログラム変更 9/2
# RaspberryPi に API として呼び出し
# http で呼び出して画像を撮って保存させる
# 夜に取得した画像を一日分圧縮してサーバに保存する

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def index():
    return 'Hello world'

@app.route('/hello')




if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=8080)
