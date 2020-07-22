import mechanize
from bs4 import BeautifulSoup


#to initialize the browser
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

kind="https://punchng.com/topics/news/"
# kind = "https://punchng.com/search/buhari"
br.open(kind)
# br.open("https://punchng.com/topics/news/")
# https://punchng.com/topics/entertainment/
# br.open("https://punchng.com/topics/business/")
# br.open("https://punchng.com/topics/sports/")
# https://punchng.com/topics/technology/

# br.open("https://punchng.com/topics/politics/page/2")
# br.open("https://punchng.com/topics/news/page/2")
# br.open("https://punchng.com/topics/business/page/2")
# br.open("https://punchng.com/topics/sports/page/2")

# br.open("https://punchng.com/search/coronavirus")



    


# saves page source
orders_html = br.response().read()

#initializing bs4 for scraping
soup = BeautifulSoup(orders_html,'html.parser')

#got the div wrapping each listed news element
list_items = soup.find_all("div", {"class": "items"})

#got the h2 tag wrapping each listed title 
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
#keys for the to create a dictionary
keys=['id','summary','date','photo','title', 'link']

_id=[]

#looping to append titles to the list
for tit in titles:
    title.append(tit.find(text=True))

# looping to make the index of each element represented by the title be the id of that news element
for i in title:
    _id.append(title.index(i))


# appending summary to list
for sum in summaries:
    random = sum.find_all('p')
    for realshit in random:
        summary.append(realshit.find(text=True))


for data in dates:
    random = data.find_all('span')
    for realshit in random:
        date.append(realshit.find(text=True))

for sfoto in imagelinks:
    smallimage.append(sfoto['data-src-small'])

for pfoto in imagelinks:
    largeimage.append(pfoto['data-src'])

for insecure in list_items:
    links = insecure.find_all('a', href=True)
    for hyper in links:
        link.append(hyper['href'])


# this converts all the lists to a dictionary
data=[]
for i in range(len(keys)):
        data.append({'id':_id[i],'summary':summary[i],'date':date[i],'photo':largeimage[i],'title':title[i],'link':link[i]})
print(data)


