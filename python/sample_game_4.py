# 3文字のアルファベットを当てるゲーム

# ゲームの構成
# 目的:3文字のアルファベットを当てる
# 行動:プレーヤーが3文字のアルファベットを入力する
# 情報:入力された文字が正しい位置にあれば■を表示する
# ＿＿:入力された文字が正解に存在すれば●を表示する
# ＿＿:入力された文字が存在しなければ○を表示する

# リスト機能を使ったW●rdleっぽい文字当てゲームを作りました

# インポートモジュール
import random

# 問題の定義
word_length = 3

# リスト生成
answer_words = []
player_words = []
results = []

# 正解となる5文字を生成する
for i in range( word_length ) :
  x = chr( random.randrange( 65 , 90 ) )
  answer_words.insert( i , x )

# 正誤表の初期化
for i in range( word_length ) :
  results.insert( i , "○" )

# 繰り返し条件:入力された文字が正しい位置にない
while player_words != answer_words :

  # 解答を求める
  print( "※終了する場合は「q」と入力" )
  message = str( word_length ) + "文字のアルファベットを入力 : "
  player_answer = input( message ).upper()
  player_words = list( player_answer )

  # 正解を求める(中断処理)
  if player_answer == "Q" :
    print( "ゲームを終了します" )
    break

  # 解答を判定する
  for i in range( word_length ) :
    if player_words[i] == answer_words[i] :
      results[i] =  "■"
    elif player_words[i] in answer_words :
      results[i] =  "●"
    else :
      results[i] =  "○"
  
  # 解答正誤を表示する
  player_answer = " ".join( player_words )
  results_list = "".join( results )

  print("--------------------")
  print( "解答 : " , player_answer )
  print( "判定 : " , results_list )
  print("--------------------")

# 正解を表示する
answer = " ".join( answer_words )
print( "正解 : " ,  answer )