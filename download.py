import requests
from selene import query
from selene.api import s
from selene.support.shared import browser  # Импорт объекта browser из Selene
from selenium import webdriver  # Импорт библиотеки Selenium для управления браузером
from selenium.webdriver.chrome.service import Service  # Импорт для работы с сервисом ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager  # Импорт менеджера для автоматической установки ChromeDriver

from os_module_script import TMP_DIR

# Создаем объект ChromeOptions для настройки браузера
options = webdriver.ChromeOptions()

# Настройки для загрузки файлов:
prefs = {
    'download.default_directory': "/Users/goncharov/MindUp/ProjectsPy/QA.GURU/qa_lesson_7/tmp",
    # Указываем путь для сохранения загружаемых файлов
    'download.prompt_for_download': False,  # Отключаем запрос подтверждения загрузки файлов
}

# Добавляем настройки загрузки (prefs) в параметры браузера (options)
options.add_experimental_option("prefs", prefs)

# Создаем экземпляр веб-драйвера Chrome с указанными параметрами:
# 1. Автоматическая установка и запуск ChromeDriver через ChromeDriverManager.
# 2. Применение настроек options.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Назначаем созданный драйвер для использования в Selene через конфигурацию browser
browser.config.driver = driver


def test_file_reading():
    # browser.open('https://github.com/pytest-dev/pytest/blob/main/README.rst')
    browser.open(TMP_DIR)
    # s('[data-testid="download-raw-button"]').click() # скачивание с помощью нажатия на кнопку
    download_url = s('[data-testid="raw-button"]').get(query.attribute('href'))

    content = requests.get('https://github.com/pytest-dev/pytest/blob/main/README.rst').content
    with open('tmp/README2.rst', 'wb') as file:
        file.write(content)

    with open('tmp/README.rst') as file:
        file_content = file.read()
        assert "test_answer" in file_content
