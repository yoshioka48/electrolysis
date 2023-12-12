import pyvisa
import time
import argparse

parser = argparse.ArgumentParser(description='コマンドライン引数で動作を分岐')
parser.add_argument('--off', help='OutputのOFF指示', action='store_true')
parser.add_argument('--volt', help='電圧の指定（値、単位）', nargs=2)
parser.add_argument('--curr', help='電流の指定（値、単位）', nargs=2)
args = parser.parse_args()

ip_address = '169.254.159.191'
port = 5025

visa_address = f'TCPIP::{ip_address}::{port}::SOCKET'
rm = pyvisa.ResourceManager()
inst = rm.open_resource(visa_address)

unitDictionary = {'V': 'A', 'mV': 'mA'}

def unitConversion(uni):
    if uni in unitDictionary:
        newUni = unitDictionary[uni]
        return newUni

def commandInput(cmd):
    inst.write(cmd)
    inst.flush()
    time.sleep(0.05)

def commandReception():
    res = inst.read_all().decode()
    return res

def off():
    cmd = "OUTP 0\r"
    commandInput(cmd)
    res = commandReception()
    print(res)

def VOLT():
    if args.volt is not None:
        volt = args.volt[0]
        unit = unitConversion(args.volt[1])
        cmd = f'VOLT {volt} {unit}\r\n'
        commandInput(cmd)
        res = commandReception()
        print(res)

def CURR():
    if args.curr is not None:
        curr = args.curr[0]
        unit = unitConversion(args.curr[1])
        cmd = f'CURR {curr} {unit}\r\n'
        commandInput(cmd)
        res = commandReception()
        print(res)

inst.open()  # リソースを開く

if args.off:
    off()
elif args.volt:
    VOLT()
elif args.curr:
    CURR()

inst.close()  # リソースを閉じる
