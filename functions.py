import json

POST_PATH = "posts.json"

def load_from_json():
    """
    Загрузка из jason файла
    """
    with open(POST_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def search_post(search_str):
    """
    Поиск поста по подстроке
    """
    posts = []
    for d in load_from_json():
        if search_str.lower() in d['content'].lower():
            posts.append(d)
    return posts


def picture_save(picture):
    filename = picture.filename
    path = f'./uploads/images{filename}'
    picture.save(path)
    return path


def add_func_post(post):
    posts = load_from_json()
    posts.append(post)
    with open(POST_PATH, 'w', encoding='utf-8') as f:
        json.dump(posts, f)
    return post

