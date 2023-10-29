#coding: utf-8
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def bbs():
    lines = []
    #with openしてcsvファイルを読み込む
    with open('articles.csv',encoding='utf-8') as f:
        lines = f.readlines() #readlinesはリスト形式でcsvの内容を返す
    #index.htmlに返す
    return render_template('index.html',lines=lines)

#postメソッドを受け取る
@app.route('/result',methods=['POST'])
def result():
    #requestでarticleとnameの値を取得する
    article = request.form['article']
    name = request.form['name']
    #csvファイルに上書きモードで書き込む
    with open('articles.csv','a',encoding='utf-8') as f:
        f.write(name + ',' + article + '\n')
    #index_result.htmlに返す
    return render_template('index_result.html',article=article,name=name)


if __name__ == '__main__':
    app.run(debug=False)
