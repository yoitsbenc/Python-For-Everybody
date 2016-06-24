import urllib
from BeautifulSoup import *


url = 'http://python-data.dr-chuck.net/known_by_Sukhvir.html'

itercount=0
while itercount<7:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')

    cnt = 0
    counts = {}
    for tag in tags:
        urltag=tag.get('href', None)
        counts[urltag]=cnt+1
        cnt = cnt+1


    for key,val in counts.items():
        if val==18:
            url = key
    print url
    itercount=itercount+1
    
    
       
        
