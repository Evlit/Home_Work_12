# Сперва импортируем класс блюпринта
from json import JSONDecodeError

from flask import Blueprint, render_template, request


# Затем создаем новый блюпринт, выбираем для него имя
from functions import picture_save, add_func_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates_name')


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@loader_blueprint.route('/post')
def add_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post():
    picture = request.files.get('picture')
    content = request.form.get('content')
    if not picture or not content:
        return 'Нет картинки или текста к ней'

    if picture.filename.split('.')[-1] not in ['jpg', 'png']:
        return 'Неверный формат файла'

    try:
        picture_path: str = '/' + picture_save(picture)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Не json файл'

    post: dict = add_func_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)
