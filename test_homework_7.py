import os
import zipfile

from openpyxl import load_workbook
from pypdf import PdfReader


def test_archive_and_verify():
    resources_dir = "resources"  # Папка с ресурсами
    pdf_path = os.path.join(resources_dir, "Python-Testing.pdf")  # Путь к PDF файлу
    xlsx_path = os.path.join(resources_dir, "example.xlsx")  # Путь к XLSX файлу
    csv_path = os.path.join(resources_dir, "example.csv")  # Путь к CSV файлу
    zip_path = os.path.join(resources_dir, "hw_archive.zip")  # Путь к ZIP архиву

    # Проверяем, существует ли папка с ресурсами
    assert os.path.exists(resources_dir), f"Папка '{resources_dir}' не существует."

    # Проверяем, существует ли PDF файл
    assert os.path.exists(pdf_path), f"PDF файл '{pdf_path}' не существует."

    # Проверяем, существует ли ZIP архив
    assert os.path.exists(zip_path), f"ZIP архив '{zip_path}' не существует."

    # Открытие ZIP-архива
    print(f"Открытие архива '{zip_path}':")
    with zipfile.ZipFile(zip_path, 'r') as archive:
        # Вывод списка файлов в архиве
        file_list = archive.namelist()
        print(f"Список файлов в архиве: {file_list}")

        # **Метод 1**: Используем `archive.open` для чтения PDF файла
        """
        Метод `archive.open`:
        - Используется, если файл большой или требуется потоковая обработка.
        - Преимущество: не извлекает файл на диск, читает его прямо из архива.
        """
        with archive.open("Python-Testing.pdf") as pdf_file:
            pdf_reader = PdfReader(pdf_file)  # Читаем PDF файл как поток
            page_text = pdf_reader.pages[10].extract_text()  # Извлекаем текст 11-й страницы (индексация с 0)
            expected_text = (
                "Learn pytest While Testing an Example Application"
            )
            assert expected_text in page_text, "Содержимое PDF файла некорректно."

        # **Метод 2**: Используем `archive.read` для чтения CSV файла
        """
        Метод `archive.read`:
        - Используется для небольших файлов, когда нужно быстро получить всё содержимое.
        - Преимущество: загружает весь файл в память, удобно для компактных файлов.
        """
        csv_content = archive.read("example.csv").decode("utf-8")  # Читаем весь файл в память
        csv_rows = [row.split(",") for row in csv_content.splitlines()]  # Разделяем на строки и столбцы
        expected_csv_data = [["name", "age", "city"], ["Petr", "35", "Kazan"], ["Elena", "28", "Novosibirsk"]]
        assert csv_rows == expected_csv_data, f"Содержимое CSV файла некорректно: {csv_rows} != {expected_csv_data}"

        # **Метод 3**: Извлекаем и проверяем содержимое XLSX файла
        """
        Метод `archive.extract`:
        - Используется, если требуется сохранить файл на диск для работы сторонних библиотек.
        - Преимущество: позволяет работать с файлами, которые сложно обработать напрямую из архива.
        """
        extracted_xlsx_path = archive.extract("example.xlsx", path="extracted")  # Извлекаем файл
        workbook = load_workbook(extracted_xlsx_path)  # Загружаем XLSX файл
        sheet = workbook.active  # Получаем активный лист
        xlsx_rows = [list(row) for row in sheet.iter_rows(values_only=True)]  # Читаем строки
        expected_xlsx_data = [["name", "age", "city"], ["Anna", 25, "Saint-Petersburg"], ["Ivan", 30, "Moscow"]]
        assert xlsx_rows == expected_xlsx_data, f"Содержимое XLSX файла некорректно: {xlsx_rows} != {expected_xlsx_data}"

    # Очистка извлечённых файлов
    if os.path.exists("extracted"):
        for root, dirs, files in os.walk("extracted", topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))  # Удаляем файлы
            for name in dirs:
                os.rmdir(os.path.join(root, name))  # Удаляем папки
        os.rmdir("extracted")  # Удаляем саму папку

    # Удаляем созданные файлы XLSX и CSV
    if os.path.exists(xlsx_path):
        os.remove(xlsx_path)  # Удаляем XLSX файл
        print(f"Удалён файл: {xlsx_path}")

    if os.path.exists(csv_path):
        os.remove(csv_path)  # Удаляем CSV файл
        print(f"Удалён файл: {csv_path}")

    # Удаляем ZIP архив
    if os.path.exists(zip_path):
        os.remove(zip_path)  # Удаляем ZIP файл
        print(f"Удалён архив: {zip_path}")
