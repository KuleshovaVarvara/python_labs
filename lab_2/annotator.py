"""
Модуль для работы с CSV-аннотацией.
"""
import csv
import os


def write_annotation(filepath: str, rows: list[tuple[str, str]]) -> None:
    """
    Записывает аннотацию в CSV.
    :param filepath: путь к CSV-файлу
    :param rows: список пар (абсолютный путь, относительный путь)
    """
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['absolute_path', 'relative_path'])
        for absolute, relative in rows:
            writer.writerow([absolute, relative])


def make_paths(filepath: str) -> tuple[str, str]:
    """
    Возвращает абсолютный и относительный путь для файла.
    :param filepath: путь к файлу
    :return: (абсолютный путь, относительный путь)
    """
    absolute = os.path.abspath(filepath)
    return (absolute, filepath)