from zipfile import ZipFile  # Импорт модуля для работы с ZIP-архивами

# Путь к ZIP-файлу
zip_path = "tmp/hello.zip"

# 1. Открытие ZIP-архива
print(f"Открытие архива '{zip_path}':")
with ZipFile(zip_path, 'r') as zip_file:
    # 2. Вывод списка файлов в архиве
    file_list = zip_file.namelist()
    print(f"Список файлов в архиве: {file_list}")

    # 3. Чтение содержимого файла 'Hello.txt' без извлечения
    file_name = 'Hello.txt'
    if file_name in file_list:
        text = zip_file.read(file_name).decode('utf-8')  # Декодируем содержимое из байт
        print(f"\nСодержимое файла '{file_name}':")
        print(text)
    else:
        print(f"\nФайл '{file_name}' не найден в архиве.")

    # 4. Извлечение файла 'Hello.txt' в директорию 'tmp'
    extract_path = '../tmp'
    print(f"\nИзвлечение файла '{file_name}' в директорию '{extract_path}':")
    zip_file.extract(file_name, path=extract_path)
    print(f"Файл '{file_name}' извлечён в директорию '{extract_path}'.")