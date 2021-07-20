import requests

TOKEN ='1780674470:AAH6Iuyeyuf4eshxGSbHsVyvXQIYG13NsI4'

BOT_URL = f'https://api.telegram.org/bot{TOKEN}'

url = f"{BOT_URL }/getMe"

result = requests.get(url)

print(result.status_code)