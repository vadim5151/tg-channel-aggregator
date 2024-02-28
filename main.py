import requests
import pprint
import os    
from dotenv import load_dotenv



def take_posts():
    pass
       

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
    text = response.json()['response']['items'][0]['text']

    all_posts = []

    for i in text:
        all_posts.append(i)

    print(''.join(all_posts))   

    data = response.json()['response']['items'][0]['attachments']
    for i in data:
        pprint.pprint(i['photo']['sizes'][-1]['url'])
        