from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello World from WSL2! with azure pipelines!"

@app.route('/version')
def version():
	return "Version 1.1"

if __name__ == '__main__':
	app.run()


