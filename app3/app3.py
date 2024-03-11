from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app3')
def blog():
    return "<body bgcolor='Tomato'> <h1 style='color:Powderblue; text-align:center  '> <u>!!! Welcome @ APP3 !!!. </u> </h1> </body>"

@app.route('/app3/hello')
def hello():
    return " <body bgcolor='Tomato'> <h1 style='color:Powderblue; text-align:center  '> <u>!!! Hello, from App3 !!!. </u> </h1> </body>"


@app.route('/app3/bye')
def bye():
    return "<body bgcolor='Tomato'> <h1 style='color:Powderblue; text-align:center  '> <u>!!!  BYE, from App3 !!!  </u> </h1> </body>"


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8083)
