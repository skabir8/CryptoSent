from flask import Flask, render_template, request, session, redirect, url_for
import os
import hashlib
import time
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

@app.route("/BTC")
def btc():
	data = utils.make_index(untils.get_tweets("btc"))
	return render_template("coin.html", coin="BTC", name="BITCOIN", data=data)

@app.route("/ETH")
def eth():
	data = utils.make_index(untils.get_tweets("eth"))
	return render_template("coin.html", coin="ETH", name="ETHEREUM", data=data)

@app.route("/BCH")
def bch():
	data = utils.make_index(untils.get_tweets("bch"))
	return render_template("coin.html", coin="BCH", name="BITCOIN CASH", data=data)

@app.route("/XRP")
def xrp():
	data = utils.make_index(untils.get_tweets("xrp"))
	return render_template("coin.html", coin="XRP", name="RIPPLE", data=data)

@app.route("/LTC")
def ltc():
	data = utils.make_index(untils.get_tweets("ltc"))
	return render_template("coin.html", coin="LTC", name="LITECOIN", data=data)

@app.route("/IOT")
def iot():
	data = utils.make_index(untils.get_tweets("iota"))
	return render_template("coin.html", coin="IOT", name="IOTA", data=data)

@app.route("/DASH")
def dash():
	data = utils.make_index(untils.get_tweets("dash"))
	return render_template("coin.html", coin="DASH", name="DASH", data=data)

@app.route("/XEM")
def xem():
	data = utils.make_index(untils.get_tweets("xem"))
	return render_template("coin.html", coin="XEM", name="NEM", data=data)

@app.route("/ADA")
def ada():
	data = utils.make_index(untils.get_tweets("ada"))
	return render_template("coin.html", coin="ADA", name="CARDANO", data=data)

@app.route("/BTG")
def btg():
	data = utils.make_index(untils.get_tweets("btg"))
	return render_template("coin.html", coin="BTG", name="BITCOIN GOLD", data=data)



if(__name__ == "__main__"):
	app.run(debug=True,host="0.0.0.0",port=8000)
