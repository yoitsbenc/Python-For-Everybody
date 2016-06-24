import urllib
import xml.etree.ElementTree as ET

url = urllib.urlopen('http://python-data.dr-chuck.net/comments_270879.xml')
xml = url.read()

stuff = ET.fromstring(xml)
lst = stuff.findall('comments/comment')

total = 0
for item in lst:
    n = item.find('count').text
    n = int(n)
    total = total + n
print total
    
