# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count):

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')

    url = tags[position-1].get('href', None)
    name =  tags[position-1].contents[0]

print(name)
