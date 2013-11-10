import requests
import json

from flask import Flask, render_template
from BeautifulSoup import BeautifulSoup

import conf

app = Flask(__name__)
OUTPUT_FILE = conf.OUTPUT_FILE

@app.route("/")
def showPage():
    return render_template('index.html')

@app.route("/up")
def isUp():

    f = open(OUTPUT_FILE,'r')
    statusJsonString = f.readlines()[0]
    f.close()

    return statusJsonString

if __name__ == "__main__":
    app.debug = conf.DEBUG
    app.host = conf.HOST
    app.port = conf.PORT
    app.run()
