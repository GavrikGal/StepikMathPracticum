import requests

url = input()

r = requests.get(url)
r.encoding = 'utf-8'


if r.status_code == 200:
    print(r.text)
else:
    print(f'Упс, произошла ошибка!..\nКод ошибки - {r.status_code}')