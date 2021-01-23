#Modules
import requests, time, sys, platform
from os import system
from bs4 import BeautifulSoup

if platform.system() == "Linux": system("clear")
else: system("cls")

#Inputs
searchme = input("Username :")
fullscan = input("Full Scan ? (Y/n) :")

if len(fullscan) < 1:
    fullscan = True
    
elif fullscan == "y":
    fullscan = True
    
elif fullscan == "n":
    fullscan = False
    
else:
    fullscan = False

#Arrays
accounts = []
others = []
socialmedia = []
maybes = []


def search(query, num):
    urls = []

    query = query.replace(' ', '+')

    URL = f"https://google.com/search?q={query}&num={num}"

    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

    headers = {"user-agent": USER_AGENT}

    resp = requests.get(URL, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        divs = soup.select("#search div.g")

        for div in divs:
            results = div.select("a")

            if (len(results) >= 1):
                urls.append(results[0].attrs['href'])

        return urls

    elif resp.status_code == 429:
        print(f"Too many requests, please try again later or use a vpn, HTTP {resp.status_code}")
        sys.exit(1)

    else:
        print(resp.status_code)
        sys.exit(1)


def basicsearch(username):
    for i in search("intext:\""+ username +"\"", num=20):
        if "user" in i:
            accounts.append(i)

        elif "twitter" in i:
            socialmedia.append(i)

        elif "instagram" in i:
            socialmedia.append(i)

        elif "github" in i:
            accounts.append(i)

        elif "spotify" in i:
            accounts.append(i)

        elif "facebook" in i:
            socialmedia.append(i)

        elif "youtube" in i:
            socialmedia.append(i)

        elif "tiktok" in i:
            socialmedia.append(i)

        elif "pinterest" in i:
            socialmedia.append(i)

        elif "snapchat" in i:
            socialmedia.append(i)

        elif "account" in i:
            socialmedia.append(i)

        elif "member" in i:
            socialmedia.append(i)

        elif "id" in i:
            socialmedia.append(i)

        elif "profile" in i:
            socialmedia.append(i)

        elif "/" + searchme in i:
            socialmedia.append(i)

        elif "/p/" in i:
            maybes.append(i)

        elif searchme in i:
            maybes.append(i)

        else:
            others.append(i)


def generalsearch(username):
    for i in search("intext:\""+ username +"\" inurl:instagram.com OR facebook.com OR linkedin.com OR twitch.tv OR snapchat.com OR tiktok.com OR pinterest.com OR youtube.com OR twitter.com", num=50):
        if username in i:
            accounts.append(i)
            
        else:
            maybes.append(i)

print("[+] Running basic search ...")

basicsearch(searchme)

print("[+] Basic search done !")

if fullscan == True:
    print("[+] Running full search, please wait it may take few minutes ...")
    time.sleep(30)
    generalsearch(searchme)

if len(others) > 0:
    print("\n[\033[1;34;m\033[34;05m*\033[25m\033[1;m] Others :\n")
    for i in others:
        print(i)
    print("-"*70)

if len(maybes) > 0:
    print("\n[\033[1;43;m\033[33;05m?\033[25m\033[1;m] Maybe :\n")
    for i in maybes:
        print(i)
    print("-"*70)

if len(accounts) > 0:
    print("\n[\033[1;32;m\033[32;05m!\033[25m\033[1;m] Found accounts :\n")
    for i in accounts:
        print(i)
    print("-"*70)

if len(others) == 0 and len(maybes) == 0 and len(accounts) == 0:
    print("\n[\033[1;32;m\033[32;05m-\033[25m\033[1;m] No result!")
