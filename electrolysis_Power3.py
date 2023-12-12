import socket
import argparse

# コマンドライン引数オプション
parser = argparse.ArgumentParser(description='コマンドライン引数で動作を分岐')

# 他の引数は省略

args = parser.parse_args()

# デバイスのホストとポート
host = '169.254.159.191'
port = 80

# ソケットを作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # ソケットをデバイスに接続
    sock.connect((host, port))

    # ここでコマンドを送信
    if args.on:
        command = 'OUTP 1\r'
        sock.sendall(command.encode())
    elif args.off:
        command = 'OUTP 0\r'
        sock.sendall(command.encode())
    elif args.idn:
        command = '*IDN?\r'
        sock.sendall(command.encode())
        data = sock.recv(1024)
        print(f'Device Info: {data.decode()}')
    elif args.volt:
        # 電圧を設定するコマンドを送信
        voltage, unit = args.volt
        command = f'VOLT {voltage} {unit}\r'
        sock.sendall(command.encode())
    elif args.curr:
        # 電流を設定するコマンドを送信
        current, unit = args.curr
        command = f'CURR {current} {unit}\r'
        sock.sendall(command.encode())
    elif args.status:
        command = '特定のステータスを確認するコマンド\r'
        sock.sendall(command.encode())
        data = sock.recv(1024)
        print(f'Device Status: {data.decode()}')
finally:
    # ソケットを閉じる
    sock.close()
