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


if(__name__ == "__main__"):
	app.run(debug=True,host="0.0.0.0",port=8000)
