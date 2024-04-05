import os
import  json 

import requests

from filter_posts import *



def send_text(tg_token,chat_id,text_post):     
    response = requests.get(f"https://api.telegram.org/bot{tg_token}/sendMessage?chat_id={chat_id}&text={text_post}")
    response.raise_for_status()


def send_photo_file(TOKEN, chat_id, img, text_post):
    file = {'photo': open(img, 'rb')}
    response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={chat_id}&caption={text_post}', files=file)
    response.raise_for_status()


def send_media_group(TOKEN, chat_id, text_post, path_to_pictures):
    media = []

    files = {}

    for i in range(len(os.listdir(path_to_pictures))):
        media.append({"type": "photo", 'media': f"attach://random-name-{i}"})
        files[media[i]['media'][9:]] = open(f"{path_to_pictures}/picture{i}.jpg", "rb")

    media[0]['caption'] = text_post

    params = {
        "chat_id": chat_id,
        "media": json.dumps(media),
        "contentType": "application/json"
    } 

    send_text = f'https://api.telegram.org/bot{TOKEN}/sendMediaGroup'
    response = requests.post(send_text, params=params, files=files)
    response.raise_for_status()


def send_video_file(TOKEN, chat_id, video):  
    file = {'video': open(video, 'rb')}
    response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendVideo?chat_id={chat_id}', files=file)
    response.raise_for_status()

    
def send_post(tg_token, chat_id, text_post, path_to_pictures):
    if len(text_post) < 1024 and  len(os.listdir(path_to_pictures)) == 1:
        send_photo_file(tg_token, chat_id, f'{path_to_pictures}/picture0.jpg',text_post) 

    if len(text_post) > 1024 and len(os.listdir(path_to_pictures)) == 1:
        send_photo_file(tg_token, chat_id, f'{path_to_pictures}/picture0.jpg',text_post[:1000])
        send_text(tg_token,chat_id,text_post[1000:])
         
    if len(os.listdir(path_to_pictures)) > 1  and  len(text_post) < 1024:
            send_media_group(tg_token, chat_id, text_post, path_to_pictures)

    if len(os.listdir(path_to_pictures)) > 1  and  len(text_post) > 1024:
            send_media_group(tg_token, chat_id, text_post, path_to_pictures)
            send_text(tg_token,chat_id,text_post[1000:])

            
def try_send_post(tg_token, chat_id, text_post, path_to_pictures):
     while True:
        try:     
            send_post(tg_token, chat_id, text_post, path_to_pictures)
            break
        except requests.exceptions.HTTPError:
            pass

