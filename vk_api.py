import requests



def generate_text_post(response):    
    text_post = response['text']
    return text_post 
    

def download_images_from_post(response):
    photo = response['attachments']
    try:
        for count, i in enumerate(photo):
            img_url = (i['photo']['sizes'][-1]['url'])
            name = f'img/picture{count}.jpg'
            r = requests.get(img_url)
            with open(name, 'wb') as file:
                file.write(r.content) 
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
    return response.json()['response']['items'][0]

