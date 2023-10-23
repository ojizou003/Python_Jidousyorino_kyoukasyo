# share.py
from flask import Flask
import glob

app = Flask(__name__)


@app.route("/")
def roote():
    files = glob.glob("static/*")
    html = '<html><meta charset="utf-8"><body>'
    html += "<h1>ファイル一覧</h1>"
    for f in files:
        html += '<P><a href="{0}">{0}</a></p>'.format(f)
    html += "</body></html>"
    return html


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
