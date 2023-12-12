import socket
import argparse

# コマンドライン引数オプション
parser = argparse.ArgumentParser(description='コマンドライン引数で動作を分岐')
parser.add_argument('action', choices=['on', 'off', 'idn', 'volt', 'curr', 'status'],
                    help='実行するアクション（on, off, idn, volt, curr, status）')
parser.add_argument('--value', nargs='*', help='値（必要に応じて）')

args = parser.parse_args()

# デバイスのホストとポート
host = '169.254.159.191'
port = 5025  # デバイスのポートに合わせて変更する

# ソケットを作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # ソケットをデバイスに接続
    sock.connect((host, port))

    # ここでコマンドを送信
    if args.action == 'on':
        command = 'OUTP 1\r'
        sock.sendall(command.encode())
    elif args.action == 'off':
        command = 'OUTP 0\r'
        sock.sendall(command.encode())
    elif args.action == 'idn':
        command = '*IDN?\r'
        sock.sendall(command.encode())
        data = sock.recv(1024)
        print(f'Device Info: {data.decode()}')
    elif args.action == 'volt' and args.value:
        # 電圧を設定するコマンドを送信
        voltage = args.value[0]
        unit = args.value[1] if len(args.value) > 1 else 'V'
        command = f'VOLT {voltage} {unit}\r'
        sock.sendall(command.encode())
    elif args.action == 'curr' and args.value:
        # 電流を設定するコマンドを送信
        current = args.value[0]
        unit = args.value[1] if len(args.value) > 1 else 'A'
        command = f'CURR {current} {unit}\r'
        sock.sendall(command.encode())
    elif args.action == 'status':
        command = '特定のステータスを確認するコマンド\r'
        sock.sendall(command.encode())
        data = sock.recv(1024)
        print(f'Device Status: {data.decode()}')
finally:
    # ソケットを閉じる
    sock.close()
