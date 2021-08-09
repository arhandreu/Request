import requests

url = 'https://superheroapi.com/api/2619421814940190/'

# Hulk, Captain America, Thanos*


def heroes_power(*names, power='intelligence'):
    hero_intelligence = {}
    for name in names:
        hero_id = requests.get(url + f"/search/{name}")
        hero_intelligence[name] = hero_id.json()['results'][0]['powerstats'][power]
    sorted_hero_intelligence = {}
    sorted_keys = sorted(hero_intelligence, key=hero_intelligence.get)
    for key in sorted_keys:
        sorted_hero_intelligence[key] = hero_intelligence[key]
    print(list(sorted_hero_intelligence.keys())[0])


heroes_power('Hulk', 'Captain America', 'Thanos')





