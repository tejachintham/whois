import subprocess
import json
l=[]
count=1
f=open("p.txt")
lines=f.readlines()
for line in lines:
    try:
        print(count)
        count=count+1
        cmd="python tes.py -s "+line
        x = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = x.communicate() 
        print(out)
        j=json.loads(out)
        expiry_date=j['expiration_date']
        creation_date=j['creation_date']
        p={
            "domain":line,
            "creation_date":creation_date,
            "expiry":expiry_date
            }    
        l.append(p)
    except:
        pass
f=open("da.txt","a")
f.write(str(l))
f.close() 
