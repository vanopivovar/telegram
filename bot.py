import requests
from time import sleep

url = "https://api.telegram.org/    /"
url_2 = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=    "
url_3 = "http://api.openweathermap.org/data/2.5/weather?q=Armavir,RU&APPID=    "

def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            weather_api = requests.post(url_3)
            meteo = weather_api.json()
            send_mess(get_chat_id(last_update(get_updates_json(url))), meteo)
            update_id += 1
            print(meteo)
            print(type(meteo))
        sleep(1)


if __name__ == '__main__':
    main()
