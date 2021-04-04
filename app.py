from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def index():
	json_test = {"1":"3"}
	return json_test

@app.route("/test")
def throw():
	return 1/0;

if __name__ == '__main__':
  app.run()