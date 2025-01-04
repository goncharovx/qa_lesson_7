import os  # Импорт модуля os для работы с файловой системой и путями
import shutil  # Импорт shutil для демонстрации рекурсивного удаления директорий

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

# Создание полного пути
base_dir = "/path/to"
file_name = "example.txt"
full_path = os.path.join(base_dir, file_name)  # Создаёт "/path/to/example.txt"
print(f"Полный путь: {full_path}")

# Проверка существования директории 'tmp' и создание, если она отсутствует
if not os.path.exists(TMP_DIR):
    os.mkdir(TMP_DIR)  # Создаём папку 'tmp'
    print(f"Папка 'tmp' создана по пути: {TMP_DIR}")
else:
    print(f"Папка 'tmp' уже существует по пути: {TMP_DIR}")

# Работа с текущей рабочей директорией
current_dir = os.getcwd()  # Возвращает текущую рабочую директорию
print(f"Текущая рабочая директория: {current_dir}")

# Проверка существования пути
absolute_path = "/Users/goncharov/MindUp/ProjectsPy/QA.GURU/qa_lesson_7"
if os.path.exists(absolute_path):
    print(f"Путь существует: {absolute_path}")
else:
    print(f"Путь не существует: {absolute_path}")

# Создание абсолютного пути из относительного
relative_path = "example_dir"
absolute_path = os.path.abspath(relative_path)
print(f"Абсолютный путь для '{relative_path}': {absolute_path}")

# Удаление директории, если она пуста
if os.path.exists(TMP_DIR):
    os.rmdir(TMP_DIR)  # Удаляет директорию (только если она пуста)
    print(f"Директория '{TMP_DIR}' удалена")
else:
    print(f"Директория '{TMP_DIR}' не существует")

# Пример shutil.rmtree
print(
    f"\nОбразовательная демонстрация: метод shutil.rmtree('{TMP_DIR}') можно использовать для удаления непустых директорий.")

# Получение списка файлов в директории
dir_name = "."
files = os.listdir(dir_name)  # Возвращает список файлов и папок в директории
print(f"Содержимое директории '{dir_name}': {files}")

# Проверка, файл это или директория
for item in os.listdir("."):
    if os.path.isfile(item):
        print(f"'{item}' — это файл")
    elif os.path.isdir(item):
        print(f"'{item}' — это директория")

# Получение имени файла и директории
path = "/path/to/example.txt"
print(f"Имя файла: {os.path.basename(path)}")  # Возвращает "example.txt"
print(f"Директория: {os.path.dirname(path)}")  # Возвращает "/path/to"

# Разделение пути
file_name, file_extension = os.path.splitext(path)
print(f"Имя файла без расширения: {file_name}")
print(f"Расширение файла: {file_extension}")

# Работа с переменными окружения
home_dir = os.getenv("HOME")  # Возвращает значение переменной окружения "HOME"
print(f"Домашняя директория: {home_dir}")

# Установка переменной окружения
os.environ["MY_VAR"] = "Hello, World!"
print(f"Моя переменная окружения: {os.getenv('MY_VAR')}")

# Удаление переменной окружения
del os.environ["MY_VAR"]
print(f"Переменная окружения 'MY_VAR' удалена")

# Выполнение команды в терминале
print("\nВыполнение команды 'ls':")
os.system("ls")

# Финальная очистка
if not os.path.exists(TMP_DIR):
    os.mkdir(TMP_DIR)  # Создаём директорию tmp для демонстрации
    print(f"Создана временная директория: {TMP_DIR}")

# Пример работы с shutil.rmtree
print("\nДемонстрация использования shutil.rmtree:")
TEST_DIR = os.path.join(CURRENT_DIR, 'test_dir')
if not os.path.exists(TEST_DIR):
    os.mkdir(TEST_DIR)
    print(f"Создана тестовая директория: {TEST_DIR}")

    # Создаём файлы в директории
    for i in range(1, 4):
        file_path = os.path.join(TEST_DIR, f"test_file_{i}.txt")
        with open(file_path, "w") as file:
            file.write(f"This is test file {i}.")
        print(f"Создан файл: {file_path}")

    print(f"Содержимое тестовой директории перед удалением: {os.listdir(TEST_DIR)}")

    # Удаляем директорию с помощью shutil.rmtree
    shutil.rmtree(TEST_DIR)
    print(f"Директория '{TEST_DIR}' успешно удалена.")
else:
    print(f"Тестовая директория '{TEST_DIR}' уже существует.")