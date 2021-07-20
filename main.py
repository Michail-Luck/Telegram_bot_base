import requests
import time

TOKEN ='1780674470:AAH6Iuyeyuf4eshxGSbHsVyvXQIYG13NsI4'

BOT_URL = f'https://api.telegram.org/bot{TOKEN}'

url = f"{BOT_URL }/getUpdates"

result = requests.get(url)

print(result.status_code)

while True:
    time.sleep(3)
    result = requests.get(url)
    messages = result.json()['result']


    for message in messages:
        chat_id = message['message']['chat']['id']
        url_send = f"{BOT_URL }/sendMessage"
        params = {
            'chat_id': chat_id ,
            'text': 'You where ?'
        }
        answer = requests.post(url_send, params = params)

