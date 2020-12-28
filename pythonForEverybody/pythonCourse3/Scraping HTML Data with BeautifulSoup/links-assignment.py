import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ('https://py4e-data.dr-chuck.net/known_by_Ateeq.html')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')

lst = list()
for tag in tags:
    lst.append(tag.get('href', None))

counter = 0
while True:
    counter = counter + 1
    url = lst[17]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    lst = list()
    if counter == 7:
        break
    for tag in tags:
        lst.append(tag.get('href', None))
    print(lst[17], counter)
#I will need a counter and a list and extract the position to be repeated 7 times at position 18 GGEZ
#it is similar to word sequnece but needs to be modified to find an index
#I will need a RE to extract the names and put them in a list and find a list index sequnece to solve it
