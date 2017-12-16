from flask import Flask, render_template, request, session, redirect, url_for
import os
import hashlib
import time
import requests_oauth2



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
	return render_template("coin.html", coin="BTC", name="BITCOIN")

@app.route("/ETH")
def eth():
	return render_template("coin.html", coin="ETH", name="ETHEREUM")

@app.route("/BCH")
def bch():
	return render_template("coin.html", coin="BCH", name="BITCOIN CASH")

@app.route("/XRP")
def xrp():
	return render_template("coin.html", coin="XRP", name="RIPPLE")

@app.route("/LTC")
def ltc():
	return render_template("coin.html", coin="LTC", name="LITECOIN")

@app.route("/IOT")
def iot():
	return render_template("coin.html", coin="IOT", name="IOTA")

@app.route("/DASH")
def dash():
	return render_template("coin.html", coin="DASH", name="DASH")

@app.route("/XEM")
def xem():
	return render_template("coin.html", coin="XEM", name="NEM")

@app.route("/ADA")
def ada():
	return render_template("coin.html", coin="ADA", name="CARDANO")

@app.route("/BTG")
def btg():
	return render_template("coin.html", coin="BTG", name="BITCOIN GOLD")



if(__name__ == "__main__"):
	app.run(debug=True,host="0.0.0.0",port=8000)
