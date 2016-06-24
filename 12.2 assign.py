import urllib
import re
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_270882.html'
html = urllib.urlopen(url).read()
print html
soup = BeautifulSoup(html)
nums = re.findall('>([0-9]+)<',html)
print nums
total = 0
for num in nums:
    intnum = int(num)
    total = total + intnum

print total
