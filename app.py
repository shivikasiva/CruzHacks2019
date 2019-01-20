from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/yolo")
def yolo():
	return "yolo"

@app.route('/greeting/<name>')
def greet(name):
	return 'Hello, {0}!'.format(name)	