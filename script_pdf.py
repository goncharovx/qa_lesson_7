import os.path  # Импорт модуля os.path для работы с путями и файловыми операциями
from pypdf import PdfReader  # Импорт PdfReader для чтения PDF-файлов

# Создаем объект PdfReader для работы с указанным PDF-файлом
reader = PdfReader('tmp/Python-Testing-with-pytest-Pragmatic-Bookshelf-2017-Brian-Okken.pdf')

# 1. Получение общего количества страниц
print(f"Общее количество страниц: {len(reader.pages)}")  # Количество страниц в PDF

# 2. Извлечение текста с конкретной страницы (например, второй)
if len(reader.pages) > 1:  # Проверяем, есть ли хотя бы 2 страницы
    print("Текст второй страницы:")
    print(reader.pages[1].extract_text())  # Отображение текста со второй страницы
else:
    print("PDF содержит менее 2 страниц.")

# 3. Извлечение текста со всех страниц
print("Текст со всех страниц PDF:")
for i, page in enumerate(reader.pages):
    print(f"Страница {i + 1}:")
    print(page.extract_text())  # Извлечение текста с каждой страницы
    print("-" * 50)  # Разделитель между страницами

# 4. Извлечение метаданных PDF
metadata = reader.metadata  # Получение метаданных документа
print("Метаданные PDF:")
print(metadata)  # Вывод всех метаданных
# Пример доступа к отдельным метаданным
print(f"Автор: {metadata.get('/Author', 'Не указан')}")
print(f"Заголовок: {metadata.get('/Title', 'Не указан')}")

# 5. Проверка защищённости PDF
print("Проверка защищённости файла:")
print(f"Файл защищён паролем: {reader.is_encrypted}")  # True, если PDF защищён паролем

# 6. Проверка наличия строки на странице
# Проверяем, содержится ли строка 'Python Testing with pytest' на второй странице
if len(reader.pages) > 1:
    assert 'Python Testing with pytest' in reader.pages[1].extract_text(), "Текст не найден на второй странице"

# 7. Получение размера PDF-файла
file_size = os.path.getsize('tmp/Python-Testing-with-pytest-Pragmatic-Bookshelf-2017-Brian-Okken.pdf')  # Размер файла в байтах
print(f"Размер файла: {file_size} байт")

# Проверка, соответствует ли размер файла ожидаемому
expected_size = 3081510
assert file_size == expected_size, f"Размер файла отличается от ожидаемого ({expected_size} байт)"

# 8. Получение размеров страницы и изображений
page = reader.pages[0]  # Первая страница
print("Информация о первой странице:")
print(f"Размер страницы (mediabox): {page.mediabox}")  # Размер страницы
print(f"Список изображений на странице: {page.images}")  # Изображения на странице (если есть)

# 9. Перебор изображений на всех страницах
print("Список изображений в документе:")
for i, page in enumerate(reader.pages):
    for image in page.images:
        print(f"Изображение на странице {i + 1}: {image}")  # Информация об изображении

# 10. Извлечение оглавления PDF
outline = reader.outline  # Возвращает оглавление документа
print("Оглавление PDF:")
print(outline)  # Вывод оглавления, если оно есть