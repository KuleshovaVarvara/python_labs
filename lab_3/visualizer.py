"""
Модуль для визуализации аудио.
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_waveform(data: np.ndarray, samplerate: int, title: str, color: str = 'blue') -> None:
    """
    Рисует график звуковой волны.
    :param data: массив сэмплов
    :param samplerate: частота дискретизации
    :param title: заголовок графика
    :param color: цвет линии
    """
    plt.figure(figsize=(10, 3))

    # Создаем ось времени (в секундах)
    time = np.arange(len(data)) / samplerate

    # Если стерео, берем только первый канал для графика, чтобы не было каши
    if len(data.shape) > 1:
        y = data[:, 0]
    else:
        y = data

    plt.plot(time, y, color=color)
    plt.title(title)
    plt.xlabel('Время (сек)')
    plt.ylabel('Амплитуда')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()