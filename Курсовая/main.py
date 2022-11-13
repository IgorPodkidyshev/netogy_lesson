import requests, json, time, os
VK_USER_ID = 28365292
VK_TOKEN = 'vk1.a.A4nnKCUOFbE5WOJPjVVgSld0T99z4auML4JhUBIDvHiHpG9GVMo3E82vwTQaSuMotMvmQGU8x_ufItd14PZQ8QHUE8u8HynjZRfcZKSEMjjW3I62xkZzMxZVIBKnK9OKOrSLM3yUsQx3eW4OESLHC79kEHCwf60g-luBy2-xKqBy0B9MOsgbufCNlI_eDBzh'
YANDEX_URL = 'https://cloud-api.yandex.net/v1/disk/resources'
YANDEX_TOKEN = 'y0_AgAAAABkznkYAAia-gAAAADT2nYMKTE7XmxYSLenvWuWANazdiOuZzM'
headers = {'Content-Type': 'application/json', 
           'Accept': 'application/json', 
           'Authorization': f'OAuth {YANDEX_TOKEN}'
           }

def GetFotoData(offset = 0, count = 10):
    api = requests.get('https://api.vk.com/method/photos.getAll', params= {
        'owner_id': VK_USER_ID,
        'access_token': VK_TOKEN,
        'extended': 1,
        'offset': offset,
        'count': count,
        'photo_sizes': 0,
        'no_service_albums': 0,
        'v': 5.131
    })
    return json.loads(api.text)
        
def GetFoto(path):
    requests.put(f'{YANDEX_URL}?path={path}', headers=headers)
    data = GetFotoData()
    count_foto = data['response']['count']
    i = 0
    number = 1
    count = 10
    fotos = []
    while i <= count_foto:
        if i != 0:
            data = GetFotoData(offset=i, count=count)
        for files in data['response']['items']:
            file_url = files['sizes'][-1]['url']
            filename_1 = file_url.split('?')[0]
            filename_2 = str(files['likes']['count']) + '_' + str(number) + filename_1.split('/')[-1][-4::]
            number += 1
            fotos.append(file_url)
            time.sleep(0.01)
            api = requests.get(file_url)
            print(filename_2) 
            
            with open('C:\\Users\\nordh\\OneDrive\\Рабочий стол\\netology\\Курсовая\\images\\%s' % filename_2, 'wb') as file:
                file.write(api.content)
            
            res = requests.get(f'{YANDEX_URL}/upload?path={path}/{filename_2}&overwrite={False}', headers=headers).json()
            with open('C:\\Users\\nordh\\OneDrive\\Рабочий стол\\netology\\Курсовая\\images\\%s' % filename_2, 'rb') as f:
                try:
                    requests.put(res['href'], files={'file':f})
                except KeyError:
                    print(res)  
            
            os.remove('C:\\Users\\nordh\\OneDrive\\Рабочий стол\\netology\\Курсовая\\images\\%s' % filename_2) 
            
            # move_foto = 
                    
        i += count


# def main():
#     GetFoto(f'PhotoVK {VK_USER_ID}')
    
# if __name__ == '__main__':
#     main()    
    
while True:
    id_user = input(f'Введите id пользователя vk:\n')
    token_yandex = input(f'Введите токен пользователя Яндекс.Диск:\n')
    VK_USER_ID = id_user
    YANDEX_TOKEN = token_yandex
    GetFoto(f'PhotoVK {id_user}')
    