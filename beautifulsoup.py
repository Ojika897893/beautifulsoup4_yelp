
#Please do not use the code because it will cause to much pressure on the Yelp website.
# The company banned me after I used this code.

#import nesseary libraries
from bs4 import BeautifulSoup
import requests

#The first page url
url = "https://www.yelp.com/search?find_desc=farmers+market&find_loc=Houston%2C+TX&cflt=farmersmarket%2Cmarkets&start=0"


for number in range(0, 80, 10): #There are eight pages with increment of 10.
    aaa = f"https://www.yelp.com/search?find_desc=farmers+market&find_loc=Houston%2C+TX&cflt=farmersmarket%2Cmarkets&start={number}"
    print(aaa) # obtain the url
    result = requests.get(aaa)
    doc = BeautifulSoup(result.text, "html.parser")
    for z in range(11): #clean the html to get only the addresses
        a = str(doc.find('script', {"type":"application/json"}))
        c = a.split("addressLines")[z]
        d = (c.find("neighborhoods"))
        e = c[:d]
        f = e.replace('"', '')
        g = f.replace(':', '')
        h = g.replace('[', '')
        i = h.replace(']', '')
        j = i.replace(',', '')
        print(j)

# online web scraping can cause too much pressure, so I decided to save the html offline and do the web scrape using google map

from bs4 import BeautifulSoup

file = open('/Users/wyattnesbit/Desktop/googlemap1-3page.html') #google map html
doc1 = BeautifulSoup(file,"html.parser")

for z in range(60): #clean the html
    entire = str(doc1.find_all('a', {"style":"cursor:pointer"}))
    c = entire.split("/data=")[z]
    d = (c.find("/maps/dir//"))
    e = c[d:]
    p_re = e.replace('+', ' ')
    map_re = p_re.replace('/maps/dir//', '')
    print(map_re)
