import requests
import pprint
import os    
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()

    url = 'https://api.vk.com/method/wall.get'

    token = os.getenv('SERVER_KEY')
    domain = 'kotrastet'
    version = 5.137

    params = {
    'access_token': token,
    'v':version,
    'domain': domain,
    'count':1
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()['response']['items']
    pprint.pprint(data)

    