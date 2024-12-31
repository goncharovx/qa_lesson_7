import os  # Импорт модуля os для работы с файловой системой и путями

"""
Модуль pathlib VS модули os и os.path в Python
https://docs-python.ru/standart-library/modul-pathlib-python/modul-pathlib-vs-moduljam-os-os-path/
"""

# Получение абсолютного пути к текущему исполняемому файлу
CURRENT_FILE = os.path.abspath(__file__)
print(CURRENT_FILE)  # Вывод абсолютного пути к текущему файлу

# Получение директории, в которой находится текущий файл
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)  # Вывод директории текущего файла

# Формирование пути к папке 'tmp' внутри директории текущего файла
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
print(TMP_DIR)  # Вывод пути к директории 'tmp'