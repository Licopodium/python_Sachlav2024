import pytest
from playwright.sync_api import sync_playwright


# Добавление опции для управления режимом headless
def pytest_addoption(parser):
    """Добавляет опцию командной строки для управления headless-режимом"""
    parser.addoption("--headless", action="store", default="true", help="Запуск тестов в headless-режиме (true/false)")


# Фикстура для запуска браузера Playwright (общий для всех тестов)
@pytest.fixture(scope="session")
def browser(pytestconfig):
    """Запускает браузер Playwright с учетом параметров"""
    headless = pytestconfig.getoption("--headless").lower() == "true"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, slow_mo=300)
        yield browser
        browser.close()


# Фикстура для создания новой страницы в браузере
@pytest.fixture(scope="function")
def page(browser):
    """Создает новую страницу перед каждым тестом"""
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
