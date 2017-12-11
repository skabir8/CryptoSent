from flask import Flask, render_template, request, session, redirect, url_for
import os
import hashlib
import time
import requests_oauth2
from utils import authorize, personalInfo, matchme, messageform, yelp, eventbrite
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.utils import secure_filename


app = Flask(__name__)


app.secret_key = "ajbddwhdajwwwwajfbsaiwfbsakqk72884bd"



@app.route("/")
def main():
	return render_template("login.html", message = message)


if(__name__ == "__main__"):
	app.run(debug=True,host="0.0.0.0",port=5000)
