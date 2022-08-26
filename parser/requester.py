import requests
import json

# with open('startups.json') as f:
#     data_list = json.load(f)
    
# for data in data_list:
#     response = requests.post('http://10.8.0.2:8000/startup/force', json=data)

with open('all_transport_articles_from_first_100_pages_techrunch.json') as f:
    data_list = json.load(f)
    
for data in data_list:
    response = requests.post('http://10.8.0.2:8000/startups', json=data)
    print(response.status_code)