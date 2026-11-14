import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """
    Фикстура: создаёт экземпляр Chrome перед тестом, закрывает после.

    :return: объект WebDriver
    """
    options = Options()
    # Если захочешь запускать без окна браузера — раскомментируй строку ниже:
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Ловит падение теста и прикрепляет к Allure-отчёту скриншот и HTML страницы.
    Это требование часто ставят в продвинутых ДЗ.
    """
    outcome = yield
    report = outcome.get_result()

    # Проверяем, что именно этап выполнения теста ('call') провалился
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            # Скриншот
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG,
            )
            # HTML страницы (чтобы видеть верстку в момент ошибки)
            allure.attach(
                driver.page_source,
                name="page_source_on_failure",
                attachment_type=allure.attachment_type.HTML,
            )
