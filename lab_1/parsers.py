"""
Модуль для разбора анкет из текста.
"""
import re
from typing import Optional


class Person:
    """
    Класс для анкеты человека.
    """

    def __init__(self, surname: str, name: str, gender: str,
                 birth_date: str, contact: str, city: str):
        self.surname = surname.strip()
        self.name = name.strip()
        self.gender = gender.strip()
        self.birth_date = birth_date.strip()
        self.contact = contact.strip()
        self.city = city.strip()


def parse_person(block: str) -> Optional[Person]:
    """
    Разбирает один блок текста в анкету.
    :param block: текст одной анкеты
    :return: объект Person или None
    """
    lines = block.strip().split('\n')
    if len(lines) < 6:
        return None

    data = {}
    for line in lines:
        if ': ' in line:
            key, value = line.split(': ', 1)
            key = key.strip()
            if key == 'Фамилия':
                data['surname'] = value
            elif key == 'Имя':
                data['name'] = value
            elif key == 'Пол':
                data['gender'] = value
            elif key == 'Дата рождения':
                data['birth_date'] = value
            elif key == 'Номер телефона или email':
                data['contact'] = value
            elif key == 'Город':
                data['city'] = value

    if len(data) == 6:
        return Person(**data)

    return None


def parse_all_people(text: str) -> list:
    """
    Разбирает весь текст на список анкет.
    :param text: весь текст с анкетами
    :return: список объектов Person
    """
    blocks = re.split(r'\n\s*\n', text.strip())
    people = []
    for block in blocks:
        if block.strip():
            person = parse_person(block)
            if person:
                people.append(person)
    return people