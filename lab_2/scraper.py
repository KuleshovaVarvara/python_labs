"""
Модуль для скачивания данных с сайта.
"""
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}


def get_html(url: str) -> str:
    """
    Скачивает HTML страницу.
    :param url: адрес страницы
    :return: текст HTML
    """
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text


def download_file(url: str, filepath: str) -> None:
    """
    Скачивает файл по ссылке и сохраняет на диск.
    :param url: ссылка на файл
    :param filepath: путь для сохранения
    """
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)