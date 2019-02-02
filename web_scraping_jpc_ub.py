import urllib3
import certifi
import os
from bs4 import BeautifulSoup

url = 'http://upkk.ub.ac.id/member/service/lowonganlist'
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
request = http.request('GET', url)
html = request.data.decode('utf-8')

soup = BeautifulSoup(html, "lxml")
lowonganlist = soup.find_all('tr')

for lowongan in lowonganlist[1:]:
    tds = lowongan.find_all('td')
    for link in tds[2].find_all('a', href=True):
        z = "%s -> %s -> %s" % (tds[1].text,tds[2].text, link['href'])
        print(z)
        #os.startfile(link['href'])