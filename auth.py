import requests
from time import sleep

with requests.Session() as session:
    print('You must know. \nYour account will use for spamming, and the programmer, who wrote this code, is not responsible for all the consequences and its further use. \nThis program was written for educational purposes.')
    print('Вы должны знать. \nВаш аккаунт будет использоваться, и программист, написавший этот код, не несёт ответственность за все последствия и дальнейшего его использования. \nЭта программа была написанна в образовательных целях.')
    login = input('Write here login - ')
    password = input('Write here password - ')
    r = session.get('https://edu.tatar.ru/logon', timeout=5)
    r.encoding = 'utf-8'
    response = session.post(
    url='https://edu.tatar.ru/logon/',
    data={
        'main_login': login,
        'main_password': password,
    },
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
    'Content-type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html',
    'Referer': 'https://edu.tatar.ru/logon',
    'Upgrade-Insecure-Requests': '1'
    },
        )
    r = session.get('https://edu.tatar.ru/logon', timeout=5)
    
    address = input('Write here facultative index - ')
    count = input('Write number of requests or "always" - ')
    spam = input('Text for spamming -')
    timer = int(input('Write number of second between requests to site - '))
    
    data = {"facultative_comment[text]":f"<p>{spam}</p>"}
    if  count == 'always':
        print("starting...")
        while True:
            r = session.post(f'https://edu.tatar.ru/facultative/index/{address}', data=data, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/html','Referer': 'https://edu.tatar.ru/logon','Upgrade-Insecure-Requests': '1'})
            sleep(timer)
        print(f'Process ended!')
    else:
        try:
            count = int(count)
            for i in range(count):
                r = session.post(f'https://edu.tatar.ru/facultative/index/{address}', data=data, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/html','Referer': 'https://edu.tatar.ru/logon','Upgrade-Insecure-Requests': '1'})
                sleep(timer)
            print(f'Process ended!')
        except Exception as e:
            print(f'Ops...\nYour number isn\'t number maybe\nError - {e}')
sleep(20)