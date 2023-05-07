# 足し算ドリル

# ゲームの構成
# 目的:ランダムな足し算問題を回答する
# 行動:問題数を指定し、出題された問題に回答する
# 情報:ランダムな足し算問題
# ＿＿:正解した問題数
# ＿＿:所要時間(今後のアップデート)

# インポートモジュール
import random

# 問題数の指定入力待ち：num_Questions
num_Questions = int(input("あなたの希望する問題数は？："))
print( "これから" , num_Questions , "問の足し算問題を出題します。それでは、ヨーイ、スタート！" )

# 初期化処理
# 使用するリスト生成
Questions = []
Answers = []
user_Answers = []
user_Results = []
user_Points = []

# 出題ループ
for i in range( num_Questions ):

  # 関数化する：make_Questions
  def make_Questions():

    # 問題の生成
    n1 = random.randrange( 10 )
    n2 = random.randrange( 10 )

    # 問題をリストに保存
    Questions.insert( i , "Q" + str( i +1) + ". " + str(n1) + "＋" + str(n2) + "＝" )

    # 正解の生成
    Answer = n1 + n2

    # 正解をリストに保存
    Answers.insert( i , Answer )

  make_Questions()

  # 関数化する:exec_Questions
  def exec_Questions():

    # 解答の入力
    user_Answer = input( Questions[i] )

    # 解答をリストに保存
    user_Answers.insert( i , user_Answer)

  exec_Questions()

# 出題の終了
print("---------- そこまで! ----------")

# 関数化する:judge_Results
def judge_Results():

  # 正誤の判定
  for i in range( num_Questions ):
    if int( user_Answers[i] ) == int( Answers[i] ):
      user_Results.insert( i , "○")
    else:
      user_Results.insert( i , "×")

judge_Results()

# ポイントの加算
for i in range( num_Questions ):
  if user_Results[i] == "○":
    user_Points.insert( i , 1 )
  else:
    user_Points.insert( i , 0 )

user_Point = sum( user_Points )

# 関数化する:view_Results
def view_Results():

  # 正誤の表示
  for i in range( num_Questions ):
    print( user_Results[i] , " : " , Questions[i] , user_Answers[i] , "……(正答：" ,Answers[i] , ")" )

# 検証結果
view_Results()

# ポイントの表示
print( "---------- あなたは全" , num_Questions , "問中、" , user_Point , "問正解しました。" )

# 成績別コメント
if user_Point == num_Questions:
  print( "---------- 素晴らしい！全問正解です。" )
elif user_Point >= num_Questions / 3:
  print( "---------- 惜しい！もう1回チャレンジしてみませんか？" )
else:
  print( "---------- にゃーん……" )