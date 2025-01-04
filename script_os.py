import os  # Импорт модуля os для работы с файловой системой и путями

"""
Модуль pathlib VS модули os и os.path в Python
https://docs-python.ru/standart-library/modul-pathlib-python/modul-pathlib-vs-moduljam-os-os-path/
"""

# Получение абсолютного пути к текущему исполняемому файлу
CURRENT_FILE = os.path.abspath(__file__)
print(f"Абсолютный путь к текущему файлу: {CURRENT_FILE}")

# Получение директории, в которой находится текущий файл
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(f"Директория текущего файла: {CURRENT_DIR}")

# Формирование пути к папке 'tmp' внутри директории текущего файла
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
print(f"Путь к папке 'tmp': {TMP_DIR}")

# Проверка существования директории 'tmp' и создание, если она отсутствует
if not os.path.exists(TMP_DIR):
    os.mkdir(TMP_DIR)  # Создаём папку 'tmp'
    print(f"Папка 'tmp' создана по пути: {TMP_DIR}")
else:
    print(f"Папка 'tmp' уже существует по пути: {TMP_DIR}")


# Абсолютный путь
absolute_path = "/Users/goncharov/MindUp/ProjectsPy/QA.GURU/qa_lesson_7"

# Проверка существования файла по абсолютному пути
if os.path.exists(absolute_path):
    print(f"Файл существует: {absolute_path}")
else:
    print(f"Файл не существует: {absolute_path}")