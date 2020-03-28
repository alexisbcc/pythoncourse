import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    # url = "http://py4e-data.dr-chuck.net/comments_42.xml"

    url = input('Enter location: ')
    if len(url) < 1: break
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    # print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('comments/comment')

    lst = [int(val.find('count').text) for val in results]
    print('Count:', len(lst))
    print('Sum:', sum(lst))
