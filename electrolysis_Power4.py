import pyvisa

# IPアドレスとポートを指定
ip_address = '169.254.159.191'
port = 5025

# VISA通信を確立
visa_address = f'TCPIP::{ip_address}::{port}::SOCKET'
rm = pyvisa.ResourceManager()
inst = rm.open_resource(visa_address)

# 以降、通常のVISA通信のコードを続ける
# 例: inst.write('OUTP 0')
#print(inst.query('*IDN?'))
#inst.write('ACQuire:STATE STOP')　ネット参考（オシロスコープ）
#inst.write('OUTP 1') #出力ON
#inst.write('OUTP 0') #出力OFF
#inst.write('VOLT 0.5')#CV時の電圧変更
#inst.write('CURR 0.1')#CC時の電流変更
#inst.write('VOLT:EXT:SOUR NONE')
