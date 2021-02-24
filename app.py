from flask import Flask
import jsonify
app = Flask(__name__)


books = [{'name': 'Snow White', 'author' : 'Grimm brothers'}, 
		{'name': 'Alice', 'author' : 'Lewis Carrol'}] 

@app.route("/")
def hello_world():
	return "Hello, world!"
	
	
	
@app.route("/api/books/titles", methods=['GET'])	
def return_all():
	return jsonify({'books':books})
	
if __name__ == "__main__":
	app.run(host="0.0.0.0.", port=80)