import requests
from bs4 import BeautifulSoup
import sys
sys.setrecursionlimit(100000)

def crawler(url):
 proxies = {'http': 'http://rahul.ranjan:69911192@202.141.80.22:3128', 'https': 'https://rahul.ranjan:69911192@202.141.80.22:3128'}
 try:
  source_code = requests.get(url,proxies=proxies)
 except requests.exceptions.SSLError:
   return
 plain_text = source_code.text
 fo = open("foo.txt", "w+")
 soup = BeautifulSoup(plain_text, "html.parser")
 for link in soup.findAll('a'):
    href = link.get('href')
    if href != None and "iitg.ernet.in" in href and "http" in href and (("home" or "index" or "pdf" or"jpg" or "png") not in href):
     print(href)
     fo.write(href+"\n")
     crawler(href)

crawler("http://intranet.iitg.ernet.in/")


