import requests

URL = "https://asky.io/api/art"
API_KEY = <your_key>

headers = {'Authorization': API_KEY}

try:
    r = requests.get(URL, headers=headers)
    response =  r.json()
except:
    print "get internet bitch!"

if len(response) > 0: print response[0]['content']
else: print "404 Not Found"
