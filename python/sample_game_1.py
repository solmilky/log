# FizzBuzz問題

# ゲームの構成
# 目的:3の倍数の時にFizzと表示する
# ＿＿:5の倍数の時にBuzzと表示する
# ＿＿:3と5の倍数の時にFizzBuzzと表示する

for number in range(1,101):
  if number % 15 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
   print(number)