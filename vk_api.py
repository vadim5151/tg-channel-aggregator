import requests



def generate_text_post(response):    
    text = response.json()['response']['items'][0]['text']
    all_text = []
    for i in text:
        all_text.append(i) 
    text_post = ''.join(all_text)
    return text_post 
    

def take_video(video_url, name):
    r = requests.get(video_url)
    with open(name, 'wb') as file:
        file.write(r.content)
   


def download_images_from_post(response):
    photo = response.json()['response']['items'][0]['attachments']
    try:
        for count, i in enumerate(photo):
            img_url = (i['photo']['sizes'][-1]['url'])
            name = f'img/picture{count}.jpg'
            r = requests.get(img_url)
            with open(name, 'wb') as file:
                file.write(r.content) 
    except KeyError:
        pass


def download_videos_from_post(response):
    video = response.json()['response']['items'][0]['attachments']
    try:
        for count, i in enumerate(video):           
            video_url = (i['video']['first_frame'][-1]['url'])
            name = f'video/video{count}.mp4'
            return video_url
            take_video(video_url, name) 
    except KeyError:
        pass


def get_last_vk_post(token, domain):
    url = 'https://api.vk.com/method/wall.get'
    session = requests.Session()
    version = 5.137
    count = 1
    params = {
        'access_token': token,
        'v':version,
        'domain': domain,
        'count':count,
    }
    response = session.get(url, params=params)
    response.raise_for_status()
    return response


