from flask import Flask
from flask import request
from flask import render_template

app = Flask(_name_)
@app.route('/')
def root():
    return render_template("index.html")

@app.route('/health')
def health():
    return "OK"

if _name_=='_main_':
    app.run(debug="true")