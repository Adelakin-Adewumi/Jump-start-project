from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'I am writing my flask api code for the first time'