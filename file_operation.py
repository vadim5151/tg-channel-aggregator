import shutil
import json
import os 



def create_folder(folder_path):   
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)


def delete_folder_img(folder_path):
    shutil.rmtree(folder_path)#удаляет папку с содержимым


def write_text_post_to_txt(text_post,file_name):
    with open(f'last_posts/{file_name}', "w", encoding="utf-8") as my_file:
        my_file.write(text_post)
        

def get_json_content(file_name):
    with open(file_name, "r", encoding="utf-8") as my_file:
        file_contents = my_file.read()
    file_contents = json.loads(file_contents)
    return file_contents