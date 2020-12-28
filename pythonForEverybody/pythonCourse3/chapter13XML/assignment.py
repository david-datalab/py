import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://py4e-data.dr-chuck.net/comments_693587.xml"
print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)#parse the data to read
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)#generate a tree
lst = tree.findall('.//comment')#search the tree for the wanted node
print('counts:', len(lst))

l = list()
for item in lst:
    value = item.find('count').text
    l.append(value)#making a list out of the values Retrieved from tree

for i in range(0, len(l)):#to convert from string to int
    l[i] = int(l[i])
s = sum(l)
print('sum:', s)
