import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
lst = list()

while True:
    address = 'https://py4e-data.dr-chuck.net/comments_693587.xml'
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    url = urllib.parse.urlencode(parms)
    print('Retrieving', url)

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)
    #results = tree.findall('count')
    result = tree.findall('.//count')
    print(result)
    #look = results[0].find('comment').find('name').find('count')
    #print(re)
    #print(data.decode())
