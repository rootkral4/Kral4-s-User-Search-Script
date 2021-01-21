import urllib

import urllib.request

import requests

import time

import sys

from bs4 import BeautifulSoup


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



accounts = []

others = []

socialmedia = []

maybes = []



def search(query, num):

    urls = []

    query = query.replace(' ', '+')

    URL = f"https://google.com/search?q={query}&num={num}"

    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

    headers = {"user-agent" : USER_AGENT}

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

        elif "spotify" in i :

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





print("\n[!] Others :\n")

for i in others:

    print(i)

print("-----")

print("\n[!] Maybe :\n")

for i in maybes:

    print(i)


print("-----")
print("\n[!] Found accounts :\n")

for i in accounts:

    print(i)

print("-----")