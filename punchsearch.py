import mechanize
from bs4 import BeautifulSoup


#to initialize the browser
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


br.open("https://punchng.com/search/coronavirus")



# saves page source
orders_html = br.response().read()

#initializing bs4 for scraping
soup = BeautifulSoup(orders_html,'html.parser')
# saves page source
orders_html = br.response().read()

#initializing bs4 for scraping
soup = BeautifulSoup(orders_html,'html.parser')

list_items = soup.find_all("div", {"class": "items"})
titles=soup.find_all("h2", {"class": "seg-title"})
summaries=soup.find_all("div", {"class": "seg-summary"})
dates=soup.find_all("div", {"class": "seg-time"})
imagelinks = soup.find_all('figure', {'class': 'seg-image'})



link=[]
title=[]
summary=[]
date=[]
smallimage=[]
largeimage=[]

for tit in titles:
    title.append(tit.find(text=True))

for sum in summaries:
    random = sum.find_all('p')
    for realshit in random:
        summary.append(realshit.find(text=True))



for data in dates:
    date.append(data(text=True))
print(date)


for sfoto in imagelinks:
    smallimage.append(sfoto['data-src-small'])

for pfoto in imagelinks:
    largeimage.append(pfoto['data-src'])

for insecure in list_items:
    links = insecure.find_all('a', href=True)
    for hyper in links:
        link.append(hyper['href'])




