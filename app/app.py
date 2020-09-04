from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

## クラスメソッド
def getDbConnection():
    '''
    DB接続
    '''
    return psycopg2.connect("postgresql://dev:pass@db:5432/dev")

def getInputs(con):
    '''
    SELECTクエリ実行→取得結果返却
    '''
    inputs = []
    with con.cursor() as cur:
        cur.execute("SELECT * FROM INPUTS")
        for row in cur:
            inputs.append("[" + str(row[1]) + "]" + row[0])
    return inputs

def insertInput(con, value):
    '''
    INSERTクエリ実行
    '''
    with con.cursor() as cur:
        cur.execute("INSERT INTO INPUTS (value, input_date) VALUES (%s,current_date)", (value, ))


## flaskルーティングメソッド
@app.route("/")
def index():
    return "Hello world!"

@app.route("/hello")
def hello():
    with getDbConnection() as con:
        return render_template("hello.html", title = "Helloページ", inputs = getInputs(con))

@app.route("/hello", methods=["POST"])
def hello_post():
    name = request.form["name"]
    message = request.form["message"]
    inputValue = name + ":" + message
    with getDbConnection() as con:
        insertInput(con, inputValue)
        return render_template("hello.html", title = "Hello(post)ページ", input1 = "入力値＝[" + inputValue + "]", inputs = getInputs(con))

@app.route("/api/hello/post", methods=["POST"])
def hello_post_ajax():
    name = request.json["name"]
    message = request.json["message"]
    inputValue = name + ":" + message
    with getDbConnection() as con:
        insertInput(con, inputValue)
    return jsonify({"input1": "入力値＝[" + inputValue + "]", "input": inputValue})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    