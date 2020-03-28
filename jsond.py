import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
#http://py4e-data.dr-chuck.net/comments_42.json
    url = input('Enter location: ')
    if len(url) < 1: break
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    # print(data.decode())

    info = json.loads(data)
    print('Count:', len(info['comments']))
    print('Sum:',sum([int(item['count']) for item in info['comments']]))
