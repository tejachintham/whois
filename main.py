from threading import Thread
import json
import time
import whois
import sys
import subprocess
from queue import Queue
concurrent = 64
def doWork():
    while True:
        url = q.get()
        urlstatus = getStatus(url)
        q.task_done()

def getStatus(myurl):
    try:
        print(myurl)
        time.sleep(0.5)
        cmd="python tes.py --site "+myurl
        x = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        stdout, stderr = x.communicate() 
        #print(stdout)
        #print(x.returncode)
        j=json.loads(stdout)
        expiry_date=j['expiration_date']
        #print(expiry_date)
        creation_date=j['creation_date']
        p={
            "domain":myurl,
            "creation_date":creation_date,
            "expiry":expiry_date
            }    
        l.append(p)
    except Exception as e:
        f=open("erro.txt","a")
        f.write(myurl)
        f.close()
        #print(e)
    f=open("lists.txt","w")
    f.write(str(l))
    f.close()     


q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    l=[]
    f=open("sites.txt")
    lines=f.readlines()
    for ll in lines:
        q.put(ll)
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
