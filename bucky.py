#this spider is basically craling webpages and collecting links 
#still has issues with redundancy of the links
#usng set can fix the issue...
#no further patch will be uploaded, a completely new spider will be uploaded.
#this is just for learning and experimenting purposes.
import requests
from bs4 import BeautifulSoup


def bucky_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = '#base URL which you want to start crawling' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('HTML marker',{'marker2': 'identification Id'}):
            href = "website url" + link.get('href')
            title = link.string
            print(title)
            print(href)

        page += 1

def single_item_data(item_url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll('HTML marker', {'marker2': 'identification Id'}):
        print(item-name.string)
    for link in soup.findAll('a'):
        href = "Website Url" + link.get('href')
        print(href)


bucky_spider(1)