import requests

proxies = {

    "http": "http://username:password@10.10.1.10:3128",
    "https": "https://username:password@10.10.1.10:1080",
}

r = requests.get('https://api64.ipify.org?format=json') 
print(r.json())