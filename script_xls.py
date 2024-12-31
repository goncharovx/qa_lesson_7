from xlrd import open_workbook  # Импорт функции open_workbook для работы с файлами Excel в формате .xls

# Открытие файла Excel
workbook = open_workbook('tmp/New XLS.xls')

# 1. Получение количества листов в книге
print(f"Количество листов в книге: {workbook.nsheets}")

# 2. Получение названий всех листов
print(f"Названия листов: {workbook.sheet_names()}")

# 3. Открытие первого листа (индексация начинается с 0)
sheet = workbook.sheet_by_index(0)
print(f"Работа с первым листом: {sheet.name}")

# 4. Получение количества строк и столбцов на листе
print(f"Количество строк на листе: {sheet.nrows}")
print(f"Количество столбцов на листе: {sheet.ncols}")

# 5. Извлечение значения из конкретной ячейки (например, B2, rowx=1, colx=1)
print(f"Значение ячейки B2: {sheet.cell_value(rowx=1, colx=1)}")

# 6. Итерация по строкам листа и вывод их содержимого
print("Содержимое строк на листе:")
for rx in range(sheet.nrows):
    print(f"Строка {rx + 1}: {sheet.row(rx)}")  # Вывод значений каждой строки

# 7. Получение значений всех ячеек в определённой строке с проверкой индекса
row_index = 2  # Пример: индекс строки, которую нужно получить
if row_index < sheet.nrows:
    print(f"Значения в строке {row_index + 1}: {sheet.row_values(row_index)}")
else:
    print(f"Ошибка: строка с индексом {row_index} отсутствует на листе. Максимальный индекс: {sheet.nrows - 1}")

# 8. Получение значений всех ячеек в определённом столбце
col_index = 1  # Например, второй столбец (индексация с 0)
if col_index < sheet.ncols:
    print(f"Значения в столбце {col_index + 1}: {sheet.col_values(col_index)}")
else:
    print(f"Ошибка: столбец с индексом {col_index} отсутствует на листе. Максимальный индекс: {sheet.ncols - 1}")

# 9. Проверка типа данных в ячейке
cell_type = sheet.cell_type(rowx=1, colx=1)  # Тип данных в ячейке B2
print(f"Тип данных ячейки B2: {cell_type}")  # Тип данных: 0 — пусто, 1 — текст, 2 — число, и т.д.

# 10. Получение всего содержимого листа
print("Весь лист как список строк:")
for row_index in range(sheet.nrows):
    print(f"Строка {row_index + 1}: {sheet.row_values(row_index)}")