from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fora')
def fora():
    return "Essa página esta fora da pasta Templates!!! 200" 

app.run(host='0.0.0.0')
