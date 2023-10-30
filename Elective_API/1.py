import requests

url = 'http://oeis.org/search'
params = {
    'q': 19673,
    # 'q' : 1234567890123456789, # Попробуйте закомментировать число
    # капрекара и раскомментировать это для эксперимента
    'fmt': 'json',
    'start': 0
}


result = set()
while(True):
    r = requests.get(url, params=params)
    if r.status_code == 200:
        Data = r.json()
        if Data['count'] == 0:
            print('В энциклопедии не нашлось, ни одной последовательности, включающей это число! =(')
            break
        else:
            for i in range(len(Data['results'])):
                print("#{} - http://oeis.org/A{}".format(Data['start'] + i + 1, Data['results'][i]['number']))
                result.add("A{}".format(Data['results'][i]['number']))
    else:
        print('ОШИБКА ' + str(r.status_code))
        break
    params['start'] += 10
    if Data['count'] - Data['start'] <= 10:
        break