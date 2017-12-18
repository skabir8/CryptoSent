from flask import Flask, render_template, request, session, redirect, url_for
import os
import hashlib
import time
import utils.queries
import utils.make_index
import utils.twitter_search



app = Flask(__name__)


app.secret_key = "ajbddwhdajwwwwajfbsaiwfbsakqk72884bd"



@app.route("/")
def main():
	return render_template("homepage.html")

@app.route("/test")
def test():
	return render_template("test.html")

@app.route("/mainform", methods=["POST"])
def mainform():
	if 'coin' not in request.form:
		return "Please select a coin"
	query = request.form['query']
	coin = request.form['coin']
	return(query + "\n" + coin)

@app.route("/BTC")
def btc():
	#ex = utils.queries.q_parse(request.form['query'])
	#matches = utils.queries.get_match(ex['and'],ex['or'],ex['not'],utils.twitter_search.get_tweets("btc"))
	#data = utils.make_index(matches)
	data = ""
	return render_template("coin.html", coin="BTC", name="BITCOIN", data=data)

@app.route("/ETH")
def eth():
	#data = utils.make_index(utils.twitter_search.get_tweets("eth"))
	data = ""
	return render_template("coin.html", coin="ETH", name="ETHEREUM", data=data)

@app.route("/BCH")
def bch():
	#data = utils.make_index(utils.twitter_search.get_tweets("bch"))
	data = ""
	return render_template("coin.html", coin="BCH", name="BITCOIN CASH", data=data)

@app.route("/XRP")
def xrp():
	#data = utils.make_index(utils.twitter_search.get_tweets("xrp"))
	data = ""
	return render_template("coin.html", coin="XRP", name="RIPPLE", data=data)

@app.route("/LTC")
def ltc():
	#data = utils.make_index(utils.twitter_search.get_tweets("ltc"))
	data = ""
	return render_template("coin.html", coin="LTC", name="LITECOIN", data=data)

@app.route("/IOT")
def iot():
	#data = utils.make_index(utils.twitter_search.get_tweets("iota"))
	data = ""
	return render_template("coin.html", coin="IOT", name="IOTA", data=data)

@app.route("/DASH")
def dash():
	#data = utils.make_index(utils.twitter_search.get_tweets("dash"))
	data = ""
	return render_template("coin.html", coin="DASH", name="DASH", data=data)

@app.route("/XEM")
def xem():
	#data = utils.make_index(utils.twitter_search.get_tweets("xem"))
	data = ""
	return render_template("coin.html", coin="XEM", name="NEM", data=data)

@app.route("/ADA")
def ada():
	#data = utils.make_index(utils.twitter_search.get_tweets("ada"))
	data = ""
	return render_template("coin.html", coin="ADA", name="CARDANO", data=data)

@app.route("/BTG")
def btg():
	#data = utils.make_index(utils.twitter_search.get_tweets("btg"))
	data = ""
	return render_template("coin.html", coin="BTG", name="BITCOIN GOLD", data=data)



if(__name__ == "__main__"):
	app.run(debug=True,host="0.0.0.0",port=8000)
