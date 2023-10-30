import requests
import zipfile

response = requests.get('https://stepik.org/media/attachments/lesson/196432/img.zip')

if response.status_code == 200:
    with open(f'img.zip', 'wb') as f:
        f.write(response.content)

    with zipfile.ZipFile('img.zip', 'r') as zip_f:
        file_list = zip_f.namelist()

    print(file_list)
