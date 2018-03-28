import urllib.request
import re

print()

ans = 'y'

while (ans == 'y' or ans == 'Y'):
    url = input("Enter YouTube URL: ")
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read().decode("utf-8")
    
    try:
        rss = re.findall(r'channel_id=(.*)"', respData)
        rss = "https://www.youtube.com/feeds/videos.xml?channel_id=" + rss[0]
        print(rss)
        print()
    except:
        print("Unable to find RSS")
        print()

    ans = input("Would you like to enter another url? ('y' or 'n'): ")
    print()
