from urllib.request import *
from urllib.error import *
from os import sys

print("""
*****************************************************************
  ___       _             _         ______                    _             
 / _ \     | |           (_)        | ___ \                  | | 
/ /_\ \  __| | _ __ ___   _  _ __   | |_/ /__ _  _ __    ___ | | 
|  _  | / _` || '_ ` _ \ | || '_ \  |  __// _` || '_ \  /___\| | 
\_| |_/ \__,_||_| |_| |_||_||_| |_| \_|   \__,_||_| |_| \___||_| 

******************************************************************                                                                                            
""")
print("[*] Includes 9500 different admin panels in list")
file = open('/root/Desktop/APF-PanelFinder/PanelList.txt', 'r')
Q = input("You have to use this program for education Y/N : ")
if Q != "Y":
    sys.exit(0)
else :
    print("You Will Continue")

link = input('Enter Website Link Correctly ex: www.google.com "  : ')
while True:
    sub_link = file.readline().split('\n')[0]

    if not sub_link:
        break
    req_link = 'http://' + link + '/' + sub_link

    try:
        response = urlopen(req_link)
    except HTTPError as e:
        continue
    except URLError as e:
        continue
    else:
        print("[+] Found => ", req_link)
