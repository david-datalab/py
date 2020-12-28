import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_693588.json"
print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)#parse the data to read
data = uh.read().decode()
info = json.loads(data)
l = list()
for item in info["comments"]:#pointing where to start extracting data , also "comments" is a list of dictionaries
    l.append(item["count"])

print('Retrieved', len(data), 'characters')
print('count:', len(info["comments"]))
print('sum:',sum(l))
