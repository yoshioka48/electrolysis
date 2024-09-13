#!/usr/bin/python3

import time
import argparse
import RPi.GPIO as GPIO

parser = argparse.ArgumentParser(description='コマンドライン引数で動作を分岐')

parser.add_argument('--sampling', help='サンプリングラインに切り替え(Pos.B)', action='store_true')
parser.add_argument('--reverse', help='廃液ラインに切り替え(Pos.A)', action='store_true')
parser.add_argument('--start', help='GCへスタート信号を送信', action='store_true')

args = parser.parse_args()

# GPIO setup
def setupGPIO(port):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(port, GPIO.OUT)

# GPIO write
def writeGPIO(port, value):
    GPIO.output(port, value)

def sampling():
    port = 17
    setupGPIO(port)
    print('port on:', port)
    writeGPIO(port, True)
    time.sleep(1)
    print('port off:', port)
    writeGPIO(port, False)
    time.sleep(1)

def reverse():
    port = 4
    setupGPIO(port)
    print('port on:', port)
    writeGPIO(port, True)
    time.sleep(1)
    print('port off:', port)
    writeGPIO(port, False)
    time.sleep(1)

def start():
    port = 27
    setupGPIO(port)
    print('port on:', port)
    writeGPIO(port, True)
    time.sleep(1)
    print('port off:', port)
    writeGPIO(port, False)
    time.sleep(1)

# 引数に応じて処理を分岐
if args.sampling:
    sampling()
elif args.reverse:
    reverse()
elif args.start:
    start()
else:
    print("引数 --sampling または --reverse を指定してください。")
