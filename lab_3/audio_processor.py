"""
Модуль для обработки аудиоданных.
"""
import numpy as np


def amplify(data: np.ndarray, factor: float) -> np.ndarray:
    """
    Увеличивает амплитуду аудио.
    :param data: массив сэмплов
    :param factor: во сколько раз увеличить
    :return: новый массив
    """
    # Умножаем все сэмплы на коэффициент
    amplified = data * factor
    # Обрезаем значения, чтобы они не вышли за пределы [-1.0, 1.0]
    return np.clip(amplified, -1.0, 1.0)


def trim(data: np.ndarray, start_sec: float, end_sec: float, sr: int) -> np.ndarray:
    """
    Обрезает аудио по времени.
    :param data: массив сэмплов
    :param start_sec: начало в секундах
    :param end_sec: конец в секундах
    :param sr: частота дискретизации
    :return: обрезанный массив
    """
    start_idx = int(start_sec * sr)
    end_idx = int(end_sec * sr)
    return data[start_idx:end_idx]


def reverse(data: np.ndarray) -> np.ndarray:
    """
    Переворачивает аудио задом наперед.
    :param data: массив сэмплов
    :return: перевернутый массив
    """
    # В numpy переворот массива делается через срез [::-1]
    return data[::-1]