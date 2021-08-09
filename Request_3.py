from datetime import date
import datetime 
import requests

now_date = datetime.datetime.strptime(str(date.today()), '%Y-%m-%d')
past_date = now_date - datetime.timedelta(days=2)

list_quest = requests.get(f'https://api.stackexchange.com/2.3/questions?fromdate={int(past_date.timestamp())}&todate={int(now_date.timestamp())}&order=desc&sort=activity&tagged=python&site=stackoverflow')

for i in range(len(list_quest.json()['items'])):
    print(f'Заголовок: "{list_quest.json()["items"][i]["title"]}" | Ссылка: {list_quest.json()["items"][i]["link"]}')









