import requests
respons = requests.get('http://api.open-notify.org/astros.json')
json = respons.json()
for person in json['people']:
    print(person['name'])