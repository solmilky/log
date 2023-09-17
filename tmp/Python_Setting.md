# Pythonの設定
たまにしか触らないため、環境構築がどこまで進んでいるのかわからなくなることが多くあります。
もっと気軽に触れるように作業ログを残します。

## 作業ログ

1. powershellにてPythonのバージョン確認を試す
   1. 実行：where python
   2. 返答：なし
   3. 判断：インストールしていない
2. pythonをインストールする
   1. インストールガイドにアクセス
      1. https://learn.microsoft.com/ja-jp/windows/python/beginners
      2. MicrosoftさんのLearnにあるのは大変ありがたい
   2. Microsoft Storeからインストール
      1. 現時点の最新版は3.11だったのでこちらを入手
   3. PowerShellでPythonのバージョンを確認
      1. 実行：where python
      2. 返答：なし（インストールの有無は関係なかったみたい）
      3. 実行：python --version
      4. 返答：Python 3.11.4
   4. パッケージマネージャーのInstallを確認
      1. 実行：pip --version
      2. 返答：pip 23.1.2 from C:\~~~~~~
   5. VSCodeのPythonをインストール
      1. Microsoftが提供している拡張機能を入手
   6. VSCodeにてインタープリターを選択
   7. VSCode上のターミナルでPythonを開き、Hello Worldを実行
      1. 実行：print("Hello, World!")
      2. 返答：Hello, World!
      3. Pythonから逃げるときはquit()
   8. Gitはインストール済みなので省略
   9. 以前作成したPythonファイルを実行してみる
      1.  python python/sample_game_1.py（FizzBuzz問題）
      2.  返答：成功。長いため省略

## 仮想環境（venv）

### 設定方法
1. 仮想環境のあるフォルダを作りたいフォルダ内で以下のコマンドを実行
   1. python -m venv [仮想環境名]
2. 1で作業したフォルダ内で、仮想環境をアクティベート
   1. .\[仮想環境名]\Scripts\activate
   2. コマンド実行後、パスの前に[仮想環境名]が表示されれば環境がアクティブになっている
3. 仮想環境のフォルダ内でpip installを行えばOK
4. 環境情報をテキストに起こす
   1. pip freeze > environment.txt
5. 出力した環境情報をインストールする時
   1. pip install -r environment.txt

### 設定した仮想環境と内容
1. pokemon_quiz
   1. flet
      1. PythonでWEBアプリケーションを開発するためのライブラリ

## Fletの使い方
1. Fletライブラリをインストールする
   1. pip install flet
2. フォルダ内でpyファイルを作成、以下コードでの使い方
3. Fletライブラリをインポートする
   1. import flet as ft
4. 
