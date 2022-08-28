from bs4 import BeautifulSoup
import requests
import json

response = requests.get('https://transport.startups-list.com/')
html_doc = response.content

def prepare_text(text):
    return text.replace("\n", "").replace("\t", "").strip().encode("ascii", "ignore").decode()

soup = BeautifulSoup(html_doc, 'html.parser')
startapps = soup.findAll(class_="startup")
json_content = []
for startapp in startapps:
    card = startapp.find(class_="main_link")
    data = {}
    data['img_link'] = card.find('img')['src']
    data['title'] = prepare_text(card.find('h1').contents[0].strip())
    data['description'] = prepare_text(card.find('p').contents[-1].strip()[:300])
    data['link'] = card['href']
    
    json_content.append(data)
    
    # response = requests.post('http://localhost:8000/startup', json=data)
    # print(data)
    # print(response.status_code)
with open('startups.json', 'w') as f:
    json.dump(json_content, f, indent=4)
