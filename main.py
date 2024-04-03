import os
from pprint import pprint  

from dotenv import load_dotenv
import requests
import time

from file_operation import *
from tg_channel import *
from filter_posts import *
from vk_api import *
from filter_posts import *
from config import *



if __name__ == '__main__':
    load_dotenv()
    
    tg_token = os.getenv('TG_TOKEN')
    server_token = os.getenv('SERVER_KEY')
    chat_id = os.getenv('CHAT_ID')

    domains = get_json_content("vk_groups.json")
    
    create_folder('last_posts')

    while True:
        for domain_number, domain in enumerate(domains):  
            response = get_last_vk_post(server_token, domain)
            create_folder('img')
            download_images_from_post(response)
            text_post = generate_text_post(response)
            if filter_post(key_words, text_post) == False:
                if os.path.isfile(f'last_posts/file{domain_number}.txt'):
                    with open(f'last_posts/file{domain_number}.txt', 'r', encoding='utf-8') as f:
                        text = f.read()
                    if text_post != text:   
                        print(123)
                        try_send_post(tg_token, chat_id, text_post)
                        write_text_post_to_txt(text_post,f'file{domain_number}.txt')     
                else:   
                    try_send_post(tg_token, chat_id, text_post)
                    write_text_post_to_txt(text_post,f'file{domain_number}.txt')
            delete_folder_img('img')
        # time.sleep(10)
            
            