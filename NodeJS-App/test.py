import requests
import sys
import json
api_key = '57c0fcb51bc74ebbb71643ef42293cdd'
business_url = ('https://newsapi.org/v2/sources?''category=business&''apiKey=57c0fcb51bc74ebbb71643ef42293cdd')
technology_url = ('https://newsapi.org/v2/sources?''category=technology&''apiKey=57c0fcb51bc74ebbb71643ef42293cdd')
sports_url = ('https://newsapi.org/v2/sources?''category=sports&''apiKey=57c0fcb51bc74ebbb71643ef42293cdd')
science_url = ('https://newsapi.org/v2/sources?''category=science&''apiKey=57c0fcb51bc74ebbb71643ef42293cdd')
health_url = ('https://newsapi.org/v2/sources?''category=health&''apiKey=57c0fcb51bc74ebbb71643ef42293cdd')
general_url = ('https://newsapi.org/v2/sources?''category=general&''apiKey=57c0fcb51bc74ebbb71643ef42293cdd')
entertainment_url = ('https://newsapi.org/v2/sources?''category=entertainment&''apiKey=57c0fcb51bc74ebbb71643ef42293cdd')


business_response = requests.get(business_url)
business_data = business_response.json()
technology_response = requests.get(technology_url)
technology_data = technology_response.json()

sports_response = requests.get(sports_url)
sports_data = sports_response.json()

science_response = requests.get(science_url)
science_data = science_response.json()

health_response = requests.get(health_url)
health_data = health_response.json()

general_response = requests.get(general_url)
general_data = general_response.json()

entertainment_response = requests.get(entertainment_url)
entertainment_data = entertainment_response.json()



