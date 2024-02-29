import os    
import shutil

from dotenv import load_dotenv
import requests



def creating_and_deleting_images_in_a_folder(folder_path):
    shutil.rmtree(folder_path)
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
    

def take_text(response):    
    text = response.json()['response']['items'][0]['text']

    all_text = []

    for i in text:
        all_text.append(i)

    print(''.join(all_text)) 

    return response     


def take_photo(response):
    photo = response.json()['response']['items'][0]['attachments']

    for count, i in enumerate(photo):
        img = (i['photo']['sizes'][-1]['url'])
        r = requests.get(img)

        with open(f'img/picture{count}.jpg', 'wb') as file:
            file.write(r.content)
            print('1')
        
        creating_and_deleting_images_in_a_folder('img') 


if __name__ == '__main__':
    load_dotenv()
    
    url = 'https://api.vk.com/method/wall.get'

    token = os.getenv('SERVER_KEY')
    domain = 'kotrastet'
    version = 5.137
    count = 1

    params = {
    'access_token': token,
    'v':version,
    'domain': domain,
    'count':count,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    take_text(response)
    take_photo(response)
       
            

    

        
        