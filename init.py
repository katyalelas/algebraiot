from flask import Flask
app = Flask(__name__)

@app.root("/")
def hello_world():
	return "Hello, world!"
