# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://py4e-data.dr-chuck.net/comments_693585.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
lst = list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    fh = tag
    #print(fh)
    for line in fh:#to extract string numbers valuse and put them in a list
        #print(line)
        num = line
        ln = re.findall("[0-9]+", num)
        for s in ln:#to loop through the strings found in ln
            #if s not in lst:#UPDATE: the headache was here XD #to add the string value in a single list
            lst.append(s)
            for i in range(0, len(lst)):#to convert from string to int
            #print(i)
                lst[i] = int(lst[i])
#print(lst)
s = sum(lst)
print(s)
