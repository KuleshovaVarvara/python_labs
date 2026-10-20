"""
Модуль для работы с файлами.
"""


def read_file(filepath: str) -> str:
    """
    Читает файл.
    :param filepath: путь к файлу
    :return: содержимое файла
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()