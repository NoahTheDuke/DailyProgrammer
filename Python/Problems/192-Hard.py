from bs4 import BeautifulSoup
from urllib.request import urlopen

pages = ['city', 'sufficiently', 'ignorance', 'isnt', 'know', 'ragdoll', 'broken', 'thaumonuclear', 'jesus', 'space', 'yantra', 'daemons', 'abstract', 'death', 'zero', 'aum', 'bare', 'people', 'deeper', 'cabal', 'protagonism', 'scrap', 'inferno', 'darkness', 'direct', 'war', 'real', 'hate', 'thursdayism', 'akheron', 'all', 'rajesh', 'machine', 'work', 'just', 'destructor']

base = 'http://qntm.org/'
for page in pages:
    soup = BeautifulSoup(urlopen(base + page).read(), "lxml")

print(soup.prettify())
p = soup.find_all(has_class_but_no_id)
print(p)
