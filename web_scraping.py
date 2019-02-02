import urllib3
import certifi
import schedule
import time
from datetime import datetime
from bs4 import BeautifulSoup

def tv_series_search():
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
        request = http.request('GET', 'https://qxr.pw/hashes/')
        html = request.data.decode('utf-8')

        soup = BeautifulSoup(html, "lxml")
        list_product = soup.find_all('a')

        isMatchFound = False
        keywords = ["person", "of", "interest"]
        #for p in list_product:
        for p in list_product[-10:]:
        #if p.text.lower().find("person") != -1:
                if all(keyword in p.text.lower() for keyword in keywords):
                        print(p.text)
                        isMatchFound = True
                        #os.startfile(p['href'])

        if not isMatchFound:
                print (str(datetime.now()),"keyword not found")

schedule.every(5).seconds.do(tv_series_search)
while 1:
        schedule.run_pending()
        time.sleep(1)


