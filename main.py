import os    

from dotenv import load_dotenv
import requests
import time

from file_operation import *
from tg_channel import *



def generate_text_post(response):    
    text = response.json()['response']['items'][0]['text']

    all_text = []

    for i in text:
        all_text.append(i) 

    text_post = ''.join(all_text)

    return text_post    


def take_photo(img,name):
    r = requests.get(img)

    with open(name, 'wb') as file:
        file.write(r.content)
    

def download_images_from_post(response):
    photo = response.json()['response']['items'][0]['attachments']
    for count, i in enumerate(photo):
        img_url = (i['photo']['sizes'][-1]['url'])
        name = f'img/picture{count}.jpg'
        take_photo(img_url, name) 


def get_last_vk_post(token, domain):
    url = 'https://api.vk.com/method/wall.get'
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
    return response


if __name__ == '__main__':
    load_dotenv()
    
    tg_token = os.getenv('TG_TOKEN')
    server_token = os.getenv('SERVER_KEY')
    chat_id = '@aggregatr0'

    domains = get_json_content("vk_groups.json")

    while True:
        for i in range(len(domains)):
            if os.path.isfile(f'last_posts/file.txt{i}'):
                print('новых постов нет')
            else:
                print(i)  
                response = get_last_vk_post(server_token, domains[i])
                create_folder('img')
                create_folder('last_posts')
                download_images_from_post(response)
                text_post = generate_text_post(response)
                write_text_post_to_txt(text_post,f'file.txt{i}')
                send_post(tg_token, chat_id, text_post )
                delete_folder_img('img')
            time.sleep(30)
            
            