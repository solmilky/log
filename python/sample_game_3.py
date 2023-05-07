# スイカ割りゲーム

# ゲームの構成
# 目的:盤面に隠されているスイカを探す
# 行動:盤面上をプレーヤーが歩き回る
# 情報:スイカとプレーヤーの距離が与えられる

# Python Japan「ゼロからのPython入門講座」より演習問題
# https://www.python.jp/train/exercise/index.html

# インポートモジュール
import random
import math

# 2点の距離を求めるローカル関数:ピタゴラスの定理
def pythagorean_theorem( x0 , y0 , x1 , y1) :
  diff_x = x0 - x1
  diff_y = y0 - y1
  return math.sqrt( diff_x ** 2 + diff_y ** 2 )

# 盤面の大きさを決める
square_num = 3

# スイカの初期位置
x = random.getrandbits(3) % square_num
y = random.getrandbits(3) % square_num
suika_location = [ x , y ]

# プレーヤーの初期位置
x = random.getrandbits(3) % square_num
y = random.getrandbits(3) % square_num
player_position = [ x , y ]

# 初期位置がスイカと被った場合に再抽選する
if suika_location == player_position :
  x = random.getrandbits(3) % square_num
  y = random.getrandbits(3) % square_num
  player_position = [ x , y ]

# 繰り返し条件:locationとpositionが異なる
while suika_location != player_position :

  # スイカからプレーヤーまでの距離を報告
  distance = round( pythagorean_theorem( suika_location[0] , suika_location[1] , player_position[0] , player_position[1] ) , 3 )
  print("スイカまで、あと約", distance ,"マスです！")

  # キーボードから文字を受け取る
  print("w :上↑に移動 / s :下↓に移動 / a :左←に移動 / d :右→に移動")
  move = input ()

  # ASWDで移動
  if move == "w" :
    player_position[0] = player_position[0] - 1
    print("上に移動しました")

  elif move == "s" :
    player_position[0] = player_position[0] + 1
    print("下に移動しました")

  elif move == "a" :
    player_position[1] = player_position[1] - 1
    print("左に移動しました")

  elif move == "d" :
    player_position[1] = player_position[1] + 1
    print("右に移動しました")
  
  print("--------------------------------------------------")

# ゲーム終了のメッセージ
print("スイカを割りました！")