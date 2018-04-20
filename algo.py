import requests
from bs4 import BeautifulSoup

fo = open("ids.txt", "w")
for i in range(10):
    url="https://nces.ed.gov/collegenavigator/?s=all&l=93&pg="+str(i)
    r=requests.get(url)

    soup=BeautifulSoup(r.content,"html.parser")
    soup.prettify()
    word=soup.find_all('td', class_="addbutton")

    for a in word:
        print(str(a)[63:69])
        
for i in range(10, 35):
    url="https://nces.ed.gov/collegenavigator/?s=all&l=93&pg="+str(i)
    r=requests.get(url)

    soup=BeautifulSoup(r.content,"html.parser")
    soup.prettify()
    word=soup.find_all('td', class_="addbutton")

    for a in word:
        print(str(a)[64:70])
        
