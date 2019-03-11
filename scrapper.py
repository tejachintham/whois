import requests
import re
from bs4 import BeautifulSoup
t=[]
linkurl=[]
resp=requests.get("https://themes.svn.wordpress.org/")
soup = BeautifulSoup(resp.text, "html.parser")
values=soup.find_all("li")
for val in values:
    links=val.find_all("a", href=True)
    for link in links:
        new_page = link.attrs["href"]
        #print(new_page)
        t.append(new_page)
f=open("scrapped.txt",'a+')
f.write(str(t))
f.close()
ver=0
for page in t:
    url="https://themes.svn.wordpress.org/"+page
    resp=requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    values=soup.find_all("li")
    val=values[-1]
    ver = val.getText()
    url="https://themes.svn.wordpress.org/"+page+"/"+ver
    try:
        url="https://themes.svn.wordpress.org/"+page+"/"+ver+"/readme.txt"
        resp=requests.get(url)
        text=resp.text
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        for url in urls:
            linkurl.append(url)
    except:
        pass
    try:
        url="https://themes.svn.wordpress.org/"+page+"/"+ver+"/README.txt"
        resp=requests.get(url)
        text=resp.text
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        for url in urls:
            linkurl.append(url)
    except:
        pass
    try:
        url="https://themes.svn.wordpress.org/"+page+"/"+ver+"/style.css"
        resp=requests.get(url)
        text=resp.text
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        for url in urls:
            linkurl.append(url)
    except:
        pass
    try:
        url="https://themes.svn.wordpress.org/"+page+"/"+ver+"/ReadMe.txt"
        resp=requests.get(url)
        text=resp.text
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        for url in urls:
            linkurl.append(url)
    except:
        pass    
f=open("linkurls.txt",'a+')
f.write(str(linkurl))
f.close()
