import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request

from functions import search_post

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates_name')


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    """
    Вывод постов по подстроке
    """
    key_search = request.args.get('s', '')
    try:
        posts = search_post(key_search)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Не json файл'
    return render_template('post_list.html', items=posts)
