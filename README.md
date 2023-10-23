# 「シゴトがはかどるPython自動処理の教科書」 クジラ飛行机 著

2023/10/16 ~ 10/23  

## Pythonで仕事を自動化しよう

バッチファイルを作り、「python 〇〇.py」と記載して、Pythonファイルと同じフォルダに格納すると、バッチファイルをダブルクリックするだけでパイソンが実行される。

## Excel作業を自動化しよう

openpyxlライブラリ(モジュール)のインストール  
pywin32は、excelがインストールされているPCでないと動かない  

インストールしたライブラリの確認(anacondaでインストールしたとき)

```Python
conda list ライブラリ名
```

Excelに数式を埋め込む場合には、値を直接指定するのではなく、'=計算式' のように '=' から始まる値を指定する

計算式ではなく計算済みの値が欲しい場合  
load_workbookメソッドにdata_only = Trueという引数を渡す

enumerate ..indexと要素を同時に取得する

表示形式の指定は、number_format

~~[$-411]~~ggge または ~~[$-ja-JP]~~ggge ..和暦年  
~~[$-411]~~dddd ..曜日(日本語)

## Excelの高度な作業も自動化しよう

設定はプログラムの先頭にまとめるのが定石

複雑そうな課題は単純な複数の工程に分割する

jsonの使い方  

```python
with open(out_file, 'wt') as fp:
    json.dump(result, fp)
```

```python
with open(in_file, 'rt') as fp:
    users = json.load(fp)
```

3つに分けたプログラムを一気に実行したい --> バッチファイルの作成

```python
REM
python read_files.py
phthon split_list.py
python gen_invoice_matome.py
PAUSE
```

- REM は "Remark"（備考）の略で、バッチファイル内でコメントを記述するために使用される  
- PAUSE はバッチファイルの実行を一時停止させるコマンド  
  一般的に、バッチファイルの実行中に結果を確認したいときや、エラーが発生した場合に、ユーザーが結果を見るために使用される  
  PAUSE コマンドの実行時、画面にメッセージが表示され、ユーザーは何かキーを押すことでバッチファイルの続行を指示する  

バッチファイルによる方法のほかに、それぞれのファイルをモジュールとして取り込む方法もある  
このときそれぞれのファイルには```__name__ == '__main__'```の記述が必要である  

ExcelとWordを連携しよう - python-docxのインストール -  

```pip install python-docx```

- doc = docx.Document() ..新規ドキュメントの作成
- doc = docx.Document('ファイル名.docx') ..既存ワードファイルの読み込み
- doc.save('ファイル名.docx')

csvファイルを読み込むときは、```encoding='sjis'```が必須

## Webブラウザの自動化／スクレイピング

必要なモジュールのインストール

- requests
- beautifulsoup4
- html5lib

selectメソッド  

```python
p = soup.select('div#eel > p.price')
print(p[0].text)
```

再帰  
関数内で同じ関数を呼び出す  
範囲の指定と訪問管理が必須  

### seleniumとChromeDriverでできること

- 任意のURLを開く
- ブラウザ履歴の操作(戻る、進む、ページ更新)
- フォームの自動送信
- 任意の要素の取得、状態の確認
- 要素のクリック、マウス操作、キーボード動作のエミュレート
- クッキーの取得や削除
- ウィンドウの位置やサイズの設定
- 指定条件まで処理の待機
- 任意のタイミングでJavaScriptを実行
- スクリーンショットの撮影

ヘッドレスモードの使い方

```python
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options = options)
```

a.get_attribute('href') はSeleniumと共に使用され、ブラウザ内のHTML要素の属性値を取得する  
一方、a['href'] はBeautiful SoupなどのHTML解析ライブラリと一緒に使用され、HTMLを解析して属性値を取得する  
選択肢はコンテキストに応じて異なる

excute_scriptメソッドの使い方

```python
# JavaScriptを実行して結果を得る
value = w = driver.excute_script('JavaScriptのコード')
```

## メールやLINE／SNSを自動化しよう

Pythonから手軽にメールを送信するには、SMTPを使うのが簡単

SMTPとは、Simple Mail Transfer Protocol

しかし、SMTP経由でのメール送信はGmailでは推奨されていない

LINE Notify を使う手順

1. LINE Notify のサイトにアクセスしてログイン
2. 送信相手先を選んでトークンを発行
3. プログラムにトークンを指定

## 業務で役立つ自動化テクニック集

社内で使える簡易Webサーバー

ちょっとダイアログ

- メッセージ表示ダイアログ
- 二択ダイアログ
- 一行入力ダイアログ
- ファイルやフォルダの選択ダイアログ

デスクトップアプリを作ってみよう

PySimpleGUI

簡単な計算ツールを作ろう

デジタル時計を作ろう

Pythonで作ったプログラムの配布  
PyInstaller

正規表現

. ..任意の1文字  
\d ..任意の数字1文字  

Pythonで正規表現を使うには、Python標準モジュールの「re」モジュールを使う

検索に関連する関数  

- m = re.match(パターン, 対象文字列) ..対象の先頭がパターンとマッチするか調べる
- m = re.search(パターン, 対象文字列) ..対象のどこかにパターンが出てくるかを調べる
- li = re.findall(パターン, 対象文字列) ..対象でマッチする部分をすべて文字列のリストで取得
- it = re.finditer(パターン, 対象文字列) ..対象でマッチする部分を探すイテレータを返す

置換や分割をする関数

- li = re.split(パターン, 対象文字列) ..対象をパターンで分割してリストで返す
- s = re.sub(パターン, 置換文字列, 対象文字列) ..対象でパターンに合致する部分を置換文字列に置換して返す

r'...' ..raw文字列 特殊文字を特殊文字として扱わない

^ ..文字列の先頭  
$ ..文字列の末尾

\ * ..直前の文字の0回以上の繰り返し  
\ + ..直前の文字の1回以上の繰り返し

? ..0回か1回繰り返す  
{m,n} ..m回以上n回以下繰り返す

[abc] ..aまたはbまたはc  
[0-9] ..数字のいずれか1文字  
[^abc] ..abc以外の1文字

(abc|def) ..abcまたはdef

\d ..数字  
\D ..数字以外  
\s ..空白文字  
\S ..空白文字以外  
\w ..英数字  
\W ..英数字以外  

マウス・キーボードの自動化  PyAutoGUI
