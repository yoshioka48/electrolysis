import pyvisa

# VISAのマネージャーを作成
rm = pyvisa.ResourceManager()

# リソースを開く
# USBデバイスのアドレスは "USB::0x0B3E::0x1029::DP002511::INST0" のように指定されることが一般的ですが、
# 実際のデバイスのアドレスに合わせて変更してください。
inst = rm.open_resource("USB::0x0B3E::0x1029::DP002511::INSTR")

# オープンが必要な場合、手動でオープンを実行する
inst.open()

# 必要に応じて操作を行う
# 例: デバイスにクエリを送信して結果を取得する
result = inst.query("*IDN?")

# 結果を表示
print("Instrument ID:", result)

# リソースを閉じる
inst.close()