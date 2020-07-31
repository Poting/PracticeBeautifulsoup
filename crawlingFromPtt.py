import requests as rq
from bs4 import BeautifulSoup
import io
import time

def sleepTime(hour, min, sec):
    return hour*3600 + min*60 + sec

doc = io.open("Biding Price.txt", "ab+") # create file to document the data, 
#ab+ : if file exist, point to the end. If not create a new one
i = 1 # start from the first page
while (i < 5): # max 4 pages
    link = "https://www.ptt.cc/bbs/Headphone/search?page=" + str(i) + "&q=airpods" # target link
    req = rq.get(link) # Use GET method
    if req.status_code == 200: # if request success
        soup = BeautifulSoup(req.text, "lxml") #change to lxml
        for post in soup.find_all('a'): # find all <a> tag 
            postTitle = post.get_text() # get the title of the post
            if "交易" in postTitle: # If the post is categorized as 'transaction'
                postLink = "https://www.ptt.cc" + post.get('href') # link of the current post
                time.sleep(3) # wait time, prevent IP blocking because of frequently request 
                contReq = rq.get(postLink) # HTTP get request
                soupCont = BeautifulSoup(contReq.text, "lxml")
                content = soupCont.find(id="main-content").get_text() # get the text of content by ID of HTML tag
                if "價格" in content: # if the "價錢" character includes in the text, write the content to a local txt file
                    doc.write(content.encode('utf-8') + '==============================='.encode('utf-8'))  # separate posts
                    doc.write('\n'.encode('utf-8')) # change line
                    time.sleep(sleeptime(0,0,3)) # sleepTime. Prevent IP blocking
    else :
        print("No More Pages") # status code != 200. Pages not exist
    i = i + 1
doc.close() # io connection close
print("ALL DONE")    

