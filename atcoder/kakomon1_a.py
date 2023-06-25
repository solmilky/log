## 2倍チェック
## 入力された3桁の数字を2倍にして出力したい
## ただし、英字が入力されるときは「error」を表示させたい

S = input()

if S.isdigit():
  S = int(S) * 2
  print(S)
else:
  print("error")

## 所要時間：30min