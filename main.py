import requests as a2,subprocess as a3,datetime as a4,platform as a5,os as a6
a7=None
status=1
def a8():
    try:return a3.check_output(["termux-battery-status"]).decode()
    except:return "Permissão negada ou Termux API não instalada"
def a9():
    try:return a3.check_output(["termux-info"]).decode()
    except:return "Permissão negada ou Termux API não instalada"
if status==1:
    a10=a4.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    a11=a8()
    a12=a9()
    a13=a5.uname()
    a14=a6.getenv("USER") or "unknown"
    a15={
        "embeds":[{
            "title":"Status Completo do Celular",
            "description":f"🕒 **Hora:** {a10}\n\n🔋 **Bateria:**\n```json\n{a11}\n```\n\n📱 **Info Termux:**\n```bash\n{a12}\n```\n\n🖥️ **Sistema:** {a13.system} {a13.release} {a13.version}\n\n👤 **Usuário:** {a14}",
            "color":0x3498db,
            "footer":{"text":"By ySixx"}
        }]
    }
    a2.post(a7,json=a15)
