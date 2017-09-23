from flask import Flask
from flask import send_file

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello this from flask"

@app.route("/")
def hello():
	try:
		return send_file('../client/index.html')
	except Exception as e:
		return str(e)