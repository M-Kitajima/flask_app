# coding: utf-8

# Import
from flask import Flask, render_template

# Flask をインスタンス化
app = Flask(__name__)

# --- View側の設定 ---
# Rootにアクセスした場合の挙動
@app.route("/")

# 以下、アクセス後の操作
def index():
    #return "Hello world!!"
    return render_template("index.html")

# entry pointの設定
if __name__ == "__main__":
     app.run()