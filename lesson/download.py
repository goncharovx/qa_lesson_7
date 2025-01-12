import os.path  # Модуль для работы с путями и файлами

import requests  # Библиотека для отправки HTTP-запросов
from selene import query  # Импорт query для работы с атрибутами элементов в Selene
from selene.api import s  # Импорт s для работы с селекторами
from selene.support.shared import browser  # Импорт объекта browser из Selene
from selenium import webdriver  # Импорт библиотеки Selenium для управления браузером
from selenium.webdriver.chrome.service import Service  # Импорт для работы с сервисом ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager  # Импорт менеджера для автоматической установки ChromeDriver

from script_os import TMP_DIR  # Импорт переменной TMP_DIR с путём временной директории


# Основной тест
def test_file_reading():
    # Создаем объект ChromeOptions для настройки браузера
    options = webdriver.ChromeOptions()

    # Настройки для загрузки файлов:
    prefs = {
        'download.default_directory': TMP_DIR,  # Указываем путь для сохранения загружаемых файлов
        'download.prompt_for_download': False,  # Отключаем запрос подтверждения загрузки файлов
    }

    # Добавляем настройки загрузки (prefs) в параметры браузера (options)
    options.add_experimental_option("prefs", prefs)

    # Создаем экземпляр веб-драйвера Chrome с указанными параметрами:
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        # Автоматическая установка и запуск ChromeDriver через ChromeDriverManager
        options=options  # Применение настроек options
    )

    # Назначаем созданный драйвер для использования в Selene через конфигурацию browser
    browser.config.driver = driver

    # Открываем страницу с README файлами Pytest на GitHub
    browser.open('https://github.com/pytest-dev/pytest/blob/main/README.rst')

    # Альтернативный способ скачать файл (раскомментировать, если нужно скачивание через нажатие кнопки)
    # s('[data-testid="download-raw-button"]').click()

    # Получаем прямую ссылку на файл через атрибут 'href' кнопки "Raw"
    download_url = s('[data-testid="raw-button"]').get(query.attribute('href'))

    # Загружаем содержимое файла с помощью HTTP-запроса
    content = requests.get(url=download_url).content

    # Сохраняем загруженный файл в директорию TMP_DIR с именем 'README.rst'
    with open(os.path.join(TMP_DIR, 'README.rst'), 'wb') as file:
        file.write(content)  # Записываем содержимое в файл в бинарном формате

    # Открываем локально сохранённый файл и читаем его содержимое
    with open('../tmp/README.rst') as file:
        file_content = file.read()  # Читаем содержимое файла в виде строки

        # Проверяем, что определённая строка присутствует в содержимом файла
        assert "test_answer" in file_content  # Если строки нет, тест упадёт с ошибкой
