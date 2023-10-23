from flask import Flask

app = Flask(__name__) #flaskオブジェクトを生成
# / へアクセスがあった場合の処理
@app.route('/')
def roote():
    return 'Hello!'

# /testへアクセスがあった場合の処理
@app.route('/test')
def test():
    return 'Test...'

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port = 5000)