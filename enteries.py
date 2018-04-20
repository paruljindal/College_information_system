import requests
from bs4 import BeautifulSoup
import csv
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

html = "https://nces.ed.gov/collegenavigator/?s=all&l=93&id="
fo = open("ids.txt", "r+")
inp = fo.readlines()
for each in inp:
    print("College id :", each.strip())
    record = []
    record.append(each.strip())
    # Getting Name and address
    x = html+str(each.strip())
    r = requests.get(x)
    soup = BeautifulSoup(r.content, "html.parser")
    soup.prettify()
    word = soup.find("span", class_="headerlg")
    record.append(str(word.get_text()))
    word = soup.find("span", style = "position:relative")
    word2 = soup.find("span", class_="disted")
    word2 = str(word2)
    word = str(word)
    word = word.replace(word2+"<br/>", "")
    word = word.replace('<br/>', '\nAddress : ')
    word = cleanhtml(word)
    record.append(word)
    word = soup.find("table", class_="layouttab")
    word = str(word)
    #word = word.replace(
    m = re.compile(r'target="_blank">(.*?)</a></td>').search(word)
    record.append(m.group(1))
    
    detect = False
    instate = False
    outstate = False
    inoncampus = False
    outoncampus = False
    word = soup.find_all("tr")
    for each1 in word:
        if "Total Expenses" in each1.get_text() or "TOTAL EXPENSES" in each1.get_text():
            detect = True
        elif detect == True:

            if "In-state" in each1.get_text() and instate == False:
                #print("In-state", file = f)
                instate = True

            elif "Out-of-state" in each1.get_text() and outstate == False:
                #print("Out-of-state", file = f)
                outstate = True
                
            elif "On Campus" in each1.get_text():
                each1 = str(each1)
                each1 = each1[::-1]
                x = each1.find('>dt<')
                y = each1.find('>dt<', x + 3)
                record.append(each1[y - 1:x + 8:-1])
                                
            elif "Off Campus with Family" in each1.get_text():
                each1 = str(each1)
                each1 = each1[::-1]
                x = each1.find('>dt<')
                y = each1.find('>dt<', x + 3)
                record.append(each1[y - 1:x + 8:-1])

            
            elif "Off Campus" in each1.get_text():
                each1 = str(each1)
                each1 = each1[::-1]
                x = each1.find('>dt<')
                y = each1.find('>dt<', x + 3)
                record.append(each1[y - 1:x + 8:-1])

    if len(record) == 7:
       record.insert(5, None)

    if len(record) == 8:
        record.insert(5, None)
        record.insert(9, None)

      
    if len(record) == 6:
        record.insert(5,None)
        record.append(None)
        record.append(None)
        
        
    with open(r'collegedata.csv', 'a', newline = '') as fp:
        a = csv.writer(fp, delimiter = ',')
        a.writerow(record)
        fp.close()        
