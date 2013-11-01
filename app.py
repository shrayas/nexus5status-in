import requests
import json

from flask import Flask, render_template
from BeautifulSoup import BeautifulSoup

app = Flask(__name__)
NEXUS5_PLAY_PAGE_URL = "https://play.google.com/store/devices/details?id=nexus_5_black_16gb"

@app.route("/")
def showPage():
    return render_template('index.html')

@app.route("/up")
def isUp():

    f = open('data.dat','r')
    statusJsonString = f.readlines()[0]

    return statusJsonString

if __name__ == "__main__":
    app.run(debug=True)
