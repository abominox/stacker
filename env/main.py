from flask import flask

app = Flask(_name_)

@app.route('/')
def index():
    return 'This is the main page!'
