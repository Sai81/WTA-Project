import requests
#url = ('https://newsapi.org/v2/top-headlines?''country=us&''apiKey=57c0fcb51bc74ebbb71643ef42293cdd')
#response = requests.get(url)

#data = response.json()

resp = {
    "Response":200,
    "Message":"Hello from python file",
    #"Data":data
}

print(json.dumps(resp))
sys.stdout.flush()