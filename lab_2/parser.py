"""
Модуль для разбора HTML.
"""
import re
from bs4 import BeautifulSoup


def get_categories(html: str) -> list[str]:
    """
    Получает ссылки на категории с главной страницы.
    :param html: HTML главной страницы
    :return: список URL категорий
    """
    soup = BeautifulSoup(html, 'html.parser')
    categories = []
    # В правой колонке — список категорий в блоке .widget
    for link in soup.select('.widget a'):
        href = link.get('href', '')
        # Нас интересуют только ссылки на категории
        if '/category/' in href or '/sound-category/' in href:
            categories.append(href)
    return categories


def get_sound_links(html: str) -> list[str]:
    """
    Находит ссылки на страницы звуков.
    :param html: HTML страницы
    :return: список URL звуков
    """
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for title_div in soup.find_all('div', class_='waveTitle'):
        a_tag = title_div.find('a')
        if a_tag and a_tag.get('href'):
            links.append(a_tag.get('href'))
    return links


def get_download_url(html: str) -> str:
    """
    Находит ссылку на скачивание аудио.
    :param html: HTML страницы звука
    :return: ссылка на скачивание или пустая строка
    """
    match = re.search(r'postid-(\d+)', html)
    if match:
        post_id = match.group(1)
        return f"https://sound-effects.ru/download-sound.php?post_id={post_id}"
    return ""