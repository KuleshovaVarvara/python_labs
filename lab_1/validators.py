"""
Модуль для проверки телефона.
"""
import re


def validate_phone(phone: str) -> bool:
    """
    Проверяет номер телефона.
    :param phone: номер
    :return: True, если номер корректный
    """
    phone = phone.strip()
    digits = re.sub(r'[()\-+\s.]', '', phone)

    if not digits.isdigit():
        return False

    if len(digits) != 11:
        return False

    if digits[0] not in ('7', '8'):
        return False

    return True