#!/usr/bin/python3

# コマンドライン引数オプション
import time
import serial
import argparse
import re

parser = argparse.ArgumentParser(description='コマンドライン引数で動作を分岐')

parser.add_argument('--on', help='OutputのON指示', action='store_true')
parser.add_argument('--off', help='OutputのON指示', action='store_true')
# --irate a b => args.irate = ['a','b']
parser.add_argument('--idn', help='device情報の確認', action='store_true')
parser.add_argument('--volt', help='電圧の指定（値、単位）', nargs=2)
parser.add_argument('--curr', help='電流の指定（値、単位）', nargs=2)
parser.add_argument('--status', help='check whether the motor is stalled or not', action='store_true')


args = parser.parse_args()

# ここから実行用コード

unitDictionary = {'V': 'A', 'mV': 'mA',}


def unitConversion(uni):
    if uni in unitDictionary:
        newUni = unitDictionary[uni]
        return newUni

# sirial通信開通
ser = serial.Serial()
ser.port = '/dev/ttyACM0'
ser.baudrate = 19200
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.parity = serial.PARITY_NONE
ser.xonxoff = False
ser.rtscts = False
ser.dsrdtr = False

cmd = "print(inst.query('*IDN?'))"
cmd = "inst.write('ACQuire:STATE STOP')" #ネット参考（オシロスコープ）
cmd = "inst.write('OUTP 1')" #出力ON
cmd = "inst.write('OUTP 0')" #出力OFF
cmd = "inst.write('VOLT 0.5')" #CV時の電圧変更
cmd = "inst.write('CURR 0.1')" #CC時の電流変更
#inst.write('VOLT:EXT:SOUR NONE')




def commandInput(cmd):  #コマンド送信
    ser.write( cmd.encode() )
    ser.flush()
    time.sleep(0.05)

def commandReception(ser):   #受信
    res=ser.read_all()
    res=res.decode()
    return res

import pyvisa

rm = pyvisa.ResourceManager()
#print(rm.list_resources())
import pyvisa
import time
from datetime import datetime


def on():
    cmd = "inst.write('OUTP 1')\r"
    commandInput(cmd)
    res=commandReception(ser)
    print(res)

def off():
    cmd = "inst.write('OUTP 0')\r"
    commandInput(cmd)
    res=commandReception(ser)
    print(res)

def VOLT(cmd):
    if args.VOLT is not None:
        volt = args.VOLT[0]
        unit = unitConversion(args.VOLT[1])
        cmd = 'VOLT ' + volt + ' ' + unit + '\r\n'
        commandInput(cmd)
        res=commandReception(ser)
        print(res)
    
def CURR(cmd):
    if args.CURR is not None:
        curr = args.CURR[0]
        unit = unitConversion(args.CURR[1])
        cmd = 'CURR ' + curr + ' ' + unit + '\r\n'
        commandInput(cmd)
        res=commandReception(ser)
        print(res)



ser.open()


if args.off:
    off()

