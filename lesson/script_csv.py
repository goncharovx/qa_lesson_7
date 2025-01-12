import csv  # Импорт стандартной библиотеки csv для работы с CSV-файлами

# 1. Чтение данных из CSV файла с использованием csv.reader
print(f"Чтение данных из файла 'New CSV.csv':")
with open('../tmp/New CSV.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"Строка: {row}")

# 2. Чтение данных из CSV файла с заголовками через csv.DictReader
print(f"\nЧтение данных из файла 'New CSV.csv' с заголовками:")
with open('../tmp/New CSV.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Строка: {row}")
        print(f"Значение столбца 'Name': {row['Name']}")

# 3. Запись данных в CSV файл с использованием csv.writer
print(f"\nЗапись данных в файл 'output.csv':")
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'San Francisco'],
]
with open('../tmp/output.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    print(f"Данные записаны в файл 'output.csv'")

# 4. Запись данных в CSV файл с заголовками через csv.DictWriter
print(f"\nЗапись данных в файл 'output_dict.csv' с заголовками:")
data_dict = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'San Francisco'},
]
with open('../tmp/output_dict.csv', mode='w', encoding='utf-8', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_dict)
    print(f"Данные записаны в файл 'output_dict.csv'")

# 5. Использование нестандартного разделителя
print(f"\nЗапись данных в файл 'output_custom.csv' с разделителем ';':")
data_custom = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'San Francisco'],
]
with open('../tmp/output_custom.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(data_custom)
    print(f"Данные записаны в файл 'output_custom.csv'")

# 6. Подсчёт строк и столбцов в CSV файле
print(f"\nПодсчёт строк и столбцов в файле 'New CSV.csv':")
with open('../tmp/New CSV.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)
    print(f"Количество строк: {len(rows)}")
    print(f"Количество столбцов: {len(rows[0]) if rows else 0}")

# 7. Пропуск пустых строк при чтении CSV
print(f"\nЧтение файла 'New CSV.csv' с пропуском пустых строк:")
with open('../tmp/New CSV.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, skipinitialspace=True)
    for row in reader:
        if any(row):
            print(f"Строка: {row}")

# 8. Поиск строки по содержимому
print(f"\nПоиск строки с определённым значением в 'New CSV.csv':")
search_value = "Alice"
with open('../tmp/New CSV.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        if search_value in row:
            print(f"Значение '{search_value}' найдено в строке {row_index + 1}: {row}")
            break
    else:
        print(f"Значение '{search_value}' не найдено.")