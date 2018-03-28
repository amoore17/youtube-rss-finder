import urllib.request
import re

print()

ans = 'y'

while (ans == 'y' or ans == 'Y'):
    url = input("Enter YouTube URL: ")
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read().decode("utf-8")
    unable_to_find = False

    try:
        rss = re.findall(r'channel_id=(.*)"', respData)
        rss = "https://www.youtube.com/feeds/videos.xml?channel_id=" + rss[0]
        print(rss)
        print()
    except:
        unable_to_find = True
        print("Unable to find RSS")
        print()

    if (unable_to_find == False):
        ans = input("Would you like to output URL to output.txt? ('y' or 'n'): ")
        if (ans == 'Y' or ans == 'y'):
            print(rss, file=open("output.txt", "a"))

    ans = input("Would you like to enter another url? ('y' or 'n'): ")
    print()
