import requests
import pytz
import datetime
import json
from BeautifulSoup import BeautifulSoup

PROXY_HOST = ""
NEXUS5_PLAY_PAGE_URL = "https://play.google.com/store/devices/details?id=nexus_5_black_16gb"

http_proxy  = https_proxy = ftp_proxy   = PROXY_HOST
proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

pageToScrape = requests.get(NEXUS5_PLAY_PAGE_URL, proxies=proxyDict)
soup = BeautifulSoup(pageToScrape.text)
notAvailTags = soup.findAll("div",{"class":"not-available"})

notAvailFlag = True
if len(notAvailTags) > 0:
    notAvailFlag = False

timeOfScrape = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

status = {}
status["status"] = notAvailFlag
status["timestamp"] = timeOfScrape.strftime("%B %d, %Y @ %I:%M%p")

print json.dumps(status)
