import requests
import json

with open('startups.json') as f:
    data_list = json.load(f)
    
for data in data_list:
    response = requests.post('https://api.drivehack.cupsoft.ru/startup/force', json=data)

with open('all_transport_articles_from_first_100_pages_techrunch.json') as f:
    data_list = json.load(f)
    
for data in data_list:
    response = requests.post('https://api.drivehack.cupsoft.ru/startups', json=data)