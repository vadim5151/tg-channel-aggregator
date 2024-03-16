import os

import requests



def send_message(tg_token,chat_id,text_post):     
    response = requests.get(f"https://api.telegram.org/bot{tg_token}/sendMessage?chat_id={chat_id}&text={text_post}")
    response.raise_for_status()


def send_photo_file(TOKEN, chat_id, img, text_post):
    file = {'photo': open(img, 'rb')}
    response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={chat_id}&caption={text_post}', files=file)
    response.raise_for_status()
                          
    
def send_post(tg_token, chat_id, text_post):
    if len(text_post) < 1024 and  len(os.listdir('img')) != 0:
        send_photo_file(tg_token, chat_id, f'img/picture0.jpg',text_post) 

    if len(text_post) > 1024 and len(os.listdir('img')) != 0:
        send_photo_file(tg_token, chat_id, f'img/picture0.jpg',text_post[:1000])
        send_message(tg_token,chat_id,text_post[1000:]) 
        
    if len(os.listdir('img')) == 0:
       send_message(tg_token,chat_id,text_post)
        
