import urllib3
import certifi
import schedule
import time
from datetime import datetime
from bs4 import BeautifulSoup


def movies_search():
    http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())
    request = http.request("GET", "https://qxr.pw/hashes/")
    html = request.data.decode("utf-8")

    soup = BeautifulSoup(html, "lxml")
    list_movie = soup.find_all("a")

    isMatchFound = False
    keyword_list = [["person", "of", "interest"], ["aquaman", "2018"], ["bumblebee", "2018"]]
    for p in list_movie[-10:]:
        for keywords in keyword_list:
            if all(keyword in p.text.lower() for keyword in keywords):
                print(str(datetime.now()), p.text)
                isMatchFound = True
                # os.startfile(p['href'])

    if not isMatchFound:
        print(str(datetime.now()), "keyword not found")
    
#schedule.every(5).seconds.do(movies_search)
schedule.every().hour.do(movies_search)
while 1:
    schedule.run_pending()
    time.sleep(1)