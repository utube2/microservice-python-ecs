from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app1')
def blog():
    return "<body bgcolor='pink'> <h1 style='color:red; text-align:center  '> <u>!!! Welcome @ APP1 !!!. </u> </h1> </body>"

@app.route('/app1/hello')
def hello():
    return " <body bgcolor='pink'> <h1 style='color:red; text-align:center  '> <u>!!! Hello, from App1 !!!. </u> </h1> </body>"


@app.route('/app1/bye')
def bye():
    return "<body bgcolor='pink'> <h1 style='color:red; text-align:center  '> <u>!!!  BYE, from App1 !!!  </u> </h1> </body>"


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)
