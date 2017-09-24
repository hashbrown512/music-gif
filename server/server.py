from flask import Flask
from flask import send_file
from flask import request
from getTimestampedGifs import get_timestamped_gifs
app = Flask(_name_)

# @app.route("/")
# def hello():
#     return "Hello this from flask"


@app.route("/")
def homepage():
	try:
		return send_file('../client/index.html')
	except Exception as e:
		return str(e)

@app.route('/song', methods = ['POST'])
def process_url():
	data = request.get_json()
	song = data["song"]
	print "song +++++++++++" + song


	# Might need to convert to Unicode

	# Need to call processing function on song

	return "hello"