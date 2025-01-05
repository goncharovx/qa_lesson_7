"""
    ========================================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    ========================================================================
"""

# Режим 'r' (read): чтение файла, файл должен существовать
with open('tmp/hello', 'r') as f:
    content = f.read()  # Читаем содержимое файла
    print(content)  # Выводим на экран

# Режим 'w' (write): запись в файл, создаёт файл, если он отсутствует, перезаписывает, если существует
with open('tmp/new_file.txt', 'w') as f:
    f.write('Hello world!')  # Записываем строку в файл

# Режим 'a' (append): добавление в конец файла, создаёт файл, если он отсутствует
with open('tmp/log.txt', 'a') as f:
    f.write('New log entry\n')  # Добавляем строку в конец файла

# Режим 'x' (exclusive creation): создаёт новый файл, вызывает ошибку, если файл уже существует
try:
    with open('tmp/unique_file.txt', 'x') as f:
        f.write('This file is created exclusively.')  # Записываем строку в новый файл
except FileExistsError:
    print('File already exists.')

# Режим 'rb' (read binary): чтение в бинарном режиме
with open('tmp/image.jpg', 'rb') as f:
    data = f.read(10)  # Читаем первые 10 байт
    print(data)  # Выводим прочитанные байты

# Режим 'wb' (write binary): запись в бинарном режиме
with open('tmp/data.bin', 'wb') as f:
    f.write(b'\x00\x01\x02\x03')  # Записываем байты в файл

# Режим 'r+' (read and write): чтение и запись, файл должен существовать
with open('tmp/hello', 'r+') as f:
    content = f.read()  # Читаем содержимое файла
    f.write('\nAdding new content.')  # Добавляем новую строку в конец файла

# Режим 'w+' (write and read): запись и чтение, файл создаётся или очищается, если уже существует
with open('tmp/new_file.txt', 'w+') as f:
    f.write('Hello world!')  # Записываем строку
    f.seek(0)  # Перемещаем курсор в начало файла
    print(f.read())  # Читаем записанное содержимое

# Режим 'a+' (append and read): добавление и чтение, создаёт файл, если он отсутствует
with open('tmp/append_file.txt', 'a+') as f:
    f.write('New entry.\n')  # Добавляем строку в конец файла
    f.seek(0)  # Перемещаем курсор в начало файла
    print(f.read())  # Читаем весь файл