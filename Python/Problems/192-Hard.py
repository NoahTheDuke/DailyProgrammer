from bs4 import BeautifulSoup
from urllib.request import urlopen

base = 'http://qntm.org'
soup = BeautifulSoup(urlopen(base + '/ra').read(), "lxml")
pages = []
for content in soup.find_all(attrs={"id": "content"}):
    for link in content.find_all('a'):
        temp = link.get('href')
        if temp[0] == '/':
            pages.append(temp)
        else:
            break

contents = ""
for idx, page in enumerate(pages):
    soup = BeautifulSoup(urlopen(base + page).read(), "lxml")
    for content in soup.find_all(attrs={"id": "content"}):
        with open('ra/{} {}.html'.format(idx, page[1:]), encoding='utf-8', mode='w') as f:
            f.write(str(soup.select("h2")[0]))
            f.write(content.prettify())
