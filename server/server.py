from flask import Flask
from flask import send_file
from flask import request
import json


app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello this from flask"

@app.route("/")
def homepage():
	try:
		return send_file('../client/giftest.html')
	except Exception as e:
		return str(e)

# @app.route('/song', methods = ['POST'])
# def process_url():

# 	print(request.form)
# 	data = request.get_json()
# 	print(data)
# 	x = json.loads(request.form)[0]
# 	print(x)
# 	# print(song)


# 	# Might need to convert to Unicode

# 	# Need to call processing function on song

# 	return "NEED TO IMPLEMENT"


@app.route('/test', methods = ['POST'])
def saveget():
	print("in process")
	a=request.args.get('song', '')
	print(a)

	# print(request.form)
	# data = request.get_json()
	# print(data)
	# x = json.loads(request.form)[0]
	# print(x)
	# print(song)


	# Might need to convert to Unicode

	# Need to call processing function on song

	print("finished")
	return "The name of the song is: " + a