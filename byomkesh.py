#!/usr/bin/python3
# Author prince kumar 
# date 27 dec 2021

import requests 
import sys
import os 
# make a help function
def help():
    print("\033[36;1m use -h or --help for the help")
    print("\033[32;1m eg. byomkesh.py username")
# make the banner function 
def banner():
    print("""\033[32;1m
 _                           _             _     
| |__  _   _  ___  _ __ ___ | | _____  ___| |__  
| '_ \\| | | |/ _ \\| '_ ` _ \\| |/ / _ \\/ __| '_ \\ 
| |_) | |_| | (_) | | | | | |   <  __/\\__ \\ | | |
|_.__/ \\__, |\\___/|_| |_| |_|_|\\_\\___||___/_| |_|
       |___/ |\033[35;1m MADE BY PRINCE                                   
""")

# make the function to check the username 
def check_user(u_name):
    # let define the some urls 
    facebook = f'https://www.facebook.com/{u_name}'
    instagram = f'https://instagram.com/{u_name}'
    twitter = f'https://www.twitter.com/{u_name}'
    youtube = f'https://www.youtube.com/{u_name}'
    blogger = f'https://{u_name}.blogspot.com'
    reddit = f'https://www.reddit.com/user/{u_name}'
    github = f'https://github.com/{u_name}'
    pinterest = f'https://www.pinterest.com/{u_name}'
    vimeo = f'https://vimeo.com/{u_name}'
    tumblr = f'https://{u_name}.tumblr.com'
    medium = f'https://medium.com/@{u_name}'
    soundcloud = f'https://soundcloud.com/{u_name}'
    spotify = f'https://open.spotify.com/user/{u_name}'
    patreon = f'https://www.patreon.com/{u_name}'
    dailymotion = f'https://www.dailymotion.com/{u_name}'
    wikipedia = f'https://www.wikipedia.org/wiki/User:{u_name}'
    # make a list os the social media accounts ...
    social_list = [facebook,instagram,twitter,youtube,blogger,github,vimeo,pinterest,tumblr,medium,soundcloud,spotify,wikipedia,patreon,dailymotion,reddit]
    # now make the requests 
    for url in social_list:
        # now make the requests 
        res = requests.get(url)
        if res.status_code == 200:
            print("\033[32;1m[~] Positive match found ")
            print(f"{url} Status code {res.status_code}")
            if u_name in res.text:
                print(f"Username {u_name} deceted in response body")
            else:
                print("\033[31;1m Username not deceted in response body")
        else:
            print("\033[31;1m username not found.", u_name,url)
            
# make a function to handle the user argument
if (len(sys.argv)<2):
    help();
elif(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
    help();
else:
    print("\033[36;1m[~] Searching the username ...")
    #passs the username to the a function 
    u_name = sys.argv[1]
    banner();
    check_user(u_name);

