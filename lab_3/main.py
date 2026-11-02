"""
Главный файл программы.
Вариант 12: (17, 18, 20) - аудио.
"""
import argparse
import os
import soundfile as sf
import numpy as np

from audio_processor import amplify, trim, reverse
from visualizer import plot_waveform


def main() -> None:
    """
    Запускает программу.
    """
    parser = argparse.ArgumentParser(description='Обработка аудио')
    parser.add_argument('input_file', type=str, help='Путь к исходному файлу')
    parser.add_argument('--output', type=str, default='result.wav', help='Путь для сохранения')
    parser.add_argument('--amp', type=float, default=1.5, help='Коэффициент усиления')
    parser.add_argument('--start', type=float, default=1.0, help='Начало обрезки (сек)')
    parser.add_argument('--end', type=float, default=3.0, help='Конец обрезки (сек)')
    args = parser.parse_args()

    try:
        # 1. Читаем файл
        print(f"Загрузка файла: {args.input_file}")
        data, samplerate = sf.read(args.input_file)

        samples_count = data.shape[0]
        channels = data.shape[1] if len(data.shape) > 1 else 1
        duration = samples_count / samplerate

        print(f"--- Информация об аудио ---")
        print(f"Количество сэмплов: {samples_count}")
        print(f"Количество каналов: {channels}")
        print(f"Частота дискретизации: {samplerate} Hz")
        print(f"Длительность: {duration:.2f} сек.")
        print(f"---------------------------")

        # 2. Показываем исходный график
        plot_waveform(data, samplerate, title='Исходный звук', color='blue')

        # 3. Применяем преобразования (Вариант 12)
        # 17. Увеличение амплитуды
        print(f"Увеличение амплитуды на {args.amp}...")
        data_amplified = amplify(data, args.amp)

        # 18. Обрезка
        print(f"Обрезка с {args.start} по {args.end} сек...")
        data_trimmed = trim(data_amplified, args.start, args.end, samplerate)

        # 20. Переворот
        print("Переворот задом наперед...")
        data_reversed = reverse(data_trimmed)

        # 4. Показываем результат
        plot_waveform(data_reversed, samplerate, title='Результат (усилен, обрезан, перевернут)', color='red')

        # 5. Сохраняем в файл
        sf.write(args.output, data_reversed, samplerate)
        print(f"Результат сохранен в: {args.output}")

    except FileNotFoundError:
        print(f"Ошибка: файл '{args.input_file}' не найден")
    except Exception as exc:
        print(f"Ошибка: {exc}")


if __name__ == '__main__':
    main()