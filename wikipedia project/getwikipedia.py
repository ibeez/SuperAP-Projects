from bs4 import BeautifulSoup 
import requests 
#get raw data from a webpage 
page = requests.get("https://en.wikipedia.org/wiki/Hamster")
#convert data into more readable text of html code
catchurch = BeautifulSoup(page.content, 'html.parser')
#print out formatted code
#print(catchurch.prettify())
def startCrawl(startlink):
    print("hello world")
def startFromBack(endlink):
    print("goodbye world")

tempfromroot = catchurch.find(accesskey="j").get('href')
links1 = requests.get('tempfromroot')
#for link in catchurch.find_all('a'):
#     print(link.get('href'))

