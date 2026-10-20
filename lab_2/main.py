"""
Главный файл программы.
Вариант 12: скачивание звуков случайных категорий.
"""
import argparse
import os
import random

from annotator import make_paths, write_annotation
from file_iterator import FileIterator
from parser import get_categories, get_download_url, get_sound_links
from scraper import download_file, get_html


def main() -> None:
    """
    Запускает программу.
    """
    parser = argparse.ArgumentParser(description='Скачивание звуков')
    parser.add_argument('--count', type=int, default=30, help='Количество звуков')
    parser.add_argument('--output', type=str, default='audio', help='Папка для сохранения')
    parser.add_argument('--annotation', type=str, default='annotation.csv', help='Путь к CSV')
    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    try:
        # 1. Получаем список категорий
        main_html = get_html('https://sound-effects.ru/')
        categories = get_categories(main_html)
        print(f"Найдено категорий: {len(categories)}")

        # 2. Перемешиваем и берём несколько
        random.shuffle(categories)
        selected = categories[:5]  # 5 случайных категорий

        # 3. Собираем ссылки на звуки из этих категорий
        all_links = []
        for cat_url in selected:
            html = get_html(cat_url)
            links = get_sound_links(html)
            all_links.extend(links)

        # 4. Перемешиваем ссылки и выбираем нужное количество
        random.shuffle(all_links)
        final_links = all_links[:args.count]

        # 5. Скачиваем
        paths = []
        for i, link in enumerate(final_links, 1):
            try:
                sound_html = get_html(link)
                download_url = get_download_url(sound_html)
                if not download_url:
                    continue
                filepath = os.path.join(args.output, f'sound_{i}.mp3')
                download_file(download_url, filepath)
                paths.append(make_paths(filepath))
                print(f"[{i}] Скачано: {filepath}")
            except Exception as exc:
                print(f"Ошибка: {exc}")

        # 6. Пишем аннотацию
        write_annotation(args.annotation, paths)
        print(f"Аннотация сохранена: {args.annotation}")

        # 7. Проверяем итератор
        print("Проверка итератора:")
        for path in FileIterator(args.annotation):
            print(f"  {path}")

    except Exception as exc:
        print(f"Общая ошибка: {exc}")


if __name__ == "__main__":
    main()