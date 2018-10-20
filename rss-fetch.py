import urllib.request
import re

to_file = ""
output_file = ""
file_exists = False

while (to_file == ""):
    print()
    to_file = input("Would you like to export your RSS feeds to a file? (\"y\" or \"n\"): ")
    
    if (to_file == "y"):
        to_file = True

        option = ""
        
        while (option == ""):
            print()
            output_file = input("Enter name of the output file: ")

            try:
                open(output_file)
                file_exists = True
            except:
                file_exists = False

            if (file_exists == True):
                print()
                print("A file of that name already exists")
                print()
                print("Would you like to: ")
                print("1. Append to file")
                print("2. Overwrite")
                print("3. Specify different name")
                print("4. Quit")
                print()
                option = int(input("Enter a number: "))

                if (option == 1):
                    f = open(output_file, "a+")
                elif (option == 2):
                    f = open(output_file, "w+")
                elif (option == 3):
                    option = ""
                    continue
                else:
                    quit()
            else:
                f = open(output_file, "w+")
                break
    elif (to_file == "n"):
        to_file = False
    else:
        to_file = ""
        print()
        print("Invalid option")
        continue

ans = 'y'

while (ans == 'y' or ans == 'Y'):
    print()
    url = input("Enter YouTube URL: ")
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read().decode("utf-8")

    # Search for RSS in the HTML
    try:
        rss = re.findall(r'channel_id=(.*)"', respData)
        rss = "https://www.youtube.com/feeds/videos.xml?channel_id=" + rss[0]
        
        if (to_file == True):
            f.write(rss + "\n")
            print()
            print("Outputted to \"" + output_file + "\"")
        else:
            print()
            print(rss)
    # Else search for RSS in the channel name
    except:
        try:
            rss = re.findall(r'/channel/(.*)', url)
            rss = "https://www.youtube.com/feeds/videos.xml?channel_id=" + rss[0]
            
            if (to_file == True):
                f.write(rss + "\n")
                print()
                print("Outputted to \"" + output_file + "\"")
            else:
                print()
                print(rss)
        except:
            print()
            print("Unable to find RSS")

    print()
    ans = input("Would you like to enter another url? ('y' or 'n'): ")

print()
