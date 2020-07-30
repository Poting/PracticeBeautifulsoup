import requests as rq
from bs4 import BeautifulSoup
import io
import time

def sleepTime(hour, min, sec):
    return hour*3600 + min*60 + sec


startTime = time.time()
file = io.open("Biding Price.txt", "ab+")
i = 1
link = "https://www.ptt.cc/bbs/Headphone/search?page=1&q=airpods"
req = rq.get(link)
soup = BeautifulSoup(req.text, "lxml")
print (soup.find_all('a')[10].get_text())
postTitle = soup.find_all('a')[10].get_text()
if "問題" in postTitle:
    print("exist")

"""
while (i <= 10):
    link = "https://www.ptt.cc/bbs/Headphone/search?page=" + str(i) + "&q=airpods"
    req = rq.get(link)
    soup = BeautifulSoup(req.text, "lxml")
    for url in soup.findAll('a', {'class': 'brand_name'})
        response = rq.get(url.get('href'))
        htmlDoc = response.text
        soup = BeautifulSoup(response.text. 'lxml')
        if soup.select('a') ! = []:
            seller = 
"""

