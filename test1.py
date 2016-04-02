import urllib
from bs4 import BeautifulSoup
import requests

url = "http://intranet.iitg.ernet.in"
urls = [url]
visited = [url]
fo = open("foo3.txt", "w+")
while len(urls) > 0:
    proxies = {'http': 'http://rahul.ranjan:69911192@202.141.80.22:3128',
               'https': 'https://rahul.ranjan:69911192@202.141.80.22:3128'}
    try:
        source_code = requests.get(urls[0], proxies=proxies)
        htmltext = source_code.text
    except requests.exceptions.SSLError:
        print(urls[0])
    soup = BeautifulSoup(htmltext, 'html.parser')
    urls.pop(0)
    for tag in soup.findAll('a',href=True):
        tag['href'] = urllib.parse.urljoin(url,tag['href'])
        if "iitg.ernet.in" in tag['href']:
            if url in tag['href'] and tag['href'] not in visited:
                fo.write(tag['href'] + "\n")
                if ".pdf" not in tag['href'] and ".zip" not in tag['href'] and ".png" not in tag['href'] and ".jpg" not in tag['href'] and ".jpeg" not in tag['href'] and "?" not in tag['href'] and "#" not in tag['href']:
                  urls.append(tag['href'])
                  visited.append(tag['href'])
                  print(tag['href'])
