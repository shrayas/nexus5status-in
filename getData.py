import requests
import pytz
import datetime
import json
from BeautifulSoup import BeautifulSoup

import conf

PROXY_HOST = conf.PROXY_HOST
TIMEOUT = conf.TIMEOUT
OUTPUT_FILE = conf.OUTPUT_FILE
NEXUS5_PLAY_PAGE_URL = conf.PAGE_URL

if len(PROXY_HOST) == 0:
    proxyDict = {}
else:
    http_proxy  = https_proxy = ftp_proxy = PROXY_HOST
    proxyDict = { 
            "http"  : "http://"+http_proxy, 
            "https" : "https://"+https_proxy, 
            "ftp"   : "ftp://"+ftp_proxy
                }

pageToScrape = requests.get(NEXUS5_PLAY_PAGE_URL, proxies=proxyDict, timeout=TIMEOUT)
soup = BeautifulSoup(pageToScrape.text)
notAvailTags = soup.findAll("div",{"class":"not-available"})

notAvailFlag = True
if len(notAvailTags) > 0:
    notAvailFlag = False

timeOfScrape = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

status = {}
status["status"] = notAvailFlag
status["timestamp"] = timeOfScrape.strftime("%B %d, %Y @ %I:%M%p")

with open(OUTPUT_FILE,'w') as f:
    f.write(json.dumps(status))
