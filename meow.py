import urllib3
import requests
import json


#Renvoie l'url vers une photo de chaton trop mignon
def meow() :
    r = requests.get('http://random.cat/meow')
    t = r.text
    a = json.loads(t)
    return a["file"]

