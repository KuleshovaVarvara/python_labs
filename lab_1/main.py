"""
Главный файл программы.
Вариант 12: ищем самый частый код оператора.
"""
import argparse
from collections import Counter
import re
from file_handler import read_file
from parsers import parse_all_people
from validators import validate_phone


def extract_operator_code(phone: str) -> str:
    """
    Достает код оператора из номера телефона.
    :param phone: номер телефона
    :return: код оператора (3 цифры после первой)
    """
    digits = re.sub(r'[()\-+\s.]', '', phone)
    return digits[1:4]


def find_most_common_operator(people: list) -> tuple:
    """
    Ищет самый частый код оператора.
    :param people: список анкет
    :return: код и сколько раз он встретился
    """
    codes = []
    for person in people:
        if validate_phone(person.contact):
            code = extract_operator_code(person.contact)
            codes.append(code)

    if not codes:
        return ('', 0)

    counter = Counter(codes)
    result = counter.most_common(1)[0]
    return result


def main() -> None:
    """
    Запускает программу.
    """
    parser = argparse.ArgumentParser(description='Поиск самого частого кода оператора')
    parser.add_argument('input_file', type=str, help='путь к файлу с анкетами')
    parser.add_argument('-o', '--output', type=str, default='result.txt',
                        help='путь к файлу для сохранения результата')
    args = parser.parse_args()

    try:
        text = read_file(args.input_file)
        people = parse_all_people(text)
        code, count = find_most_common_operator(people)

        if count == 0:
            print("Не найдено ни одного корректного номера телефона")
        else:
            print(f"Самый частый код оператора: {code}")
            print(f"Количество повторений: {count}")

        with open(args.output, 'w', encoding='utf-8') as file:
            if count == 0:
                file.write("Не найдено ни одного корректного номера телефона\n")
            else:
                file.write(f"Самый частый код оператора: {code}\n")
                file.write(f"Количество повторений: {count}\n")

        print(f"\nРезультат сохранен в файл: {args.output}")

    except FileNotFoundError:
        print(f"Ошибка: файл '{args.input_file}' не найден")
    except Exception as exc:
        print(f"Ошибка: {exc}")


if __name__ == "__main__":
    main()