from flask import Flask

app = Flask(__name__)

# Codigo modificado
@app.route('/')
def hello_world():
	return "Hello World from WSL2! with azure pipelines!"

# Segunda linea de codigo modificado 
@app.route('/version')
def version():
	return "<h3>Version 1.1</h3>"


if __name__ == '__main__':
	app.run()


