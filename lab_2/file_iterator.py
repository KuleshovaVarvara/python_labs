"""
Модуль с итератором по путям к файлам.
"""
import csv
import os


class FileIterator:
    """
    Итератор по путям к файлам.
    Может принимать либо CSV-файл, либо папку.
    """

    def __init__(self, source: str) -> None:
        """
        Инициализирует итератор.
        :param source: путь к CSV-аннотации или к папке
        """
        self.paths = []
        if source.endswith('.csv'):
            # загружаем из CSV
            with open(source, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # пропускаем заголовки
                for row in reader:
                    self.paths.append(row[1])  # относительный путь
        else:
            # загружаем из папки
            for name in os.listdir(source):
                full = os.path.join(source, name)
                if os.path.isfile(full):
                    self.paths.append(full)
        self.index = 0

    def __iter__(self) -> 'FileIterator':
        """
        Возвращает сам итератор.
        """
        return self

    def __next__(self) -> str:
        """
        Возвращает следующий путь.
        """
        if self.index < len(self.paths):
            path = self.paths[self.index]
            self.index += 1
            return path
        else:
            raise StopIteration