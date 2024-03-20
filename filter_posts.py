import os



def filtiring_posts(key_words):
    for file in os.listdir('last_posts'):
        with open(f'last_posts/{file}', "r",  encoding="utf-8") as my_file:
            for i in key_words:
                if i.lower() in my_file.read().lower():
                    response = "реклама обнаружена"
                    return response
                else:
                    response = 'рекламы нет'  
                    return response 
            # return any([i.lower() in my_file.read().lower() for i in key_words  ])
        

key_words = ['реклама', 'рекламный', 'спонсор', 'купите', 'советуем', 'рекла', 'спонс']






