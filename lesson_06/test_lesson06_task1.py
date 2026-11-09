import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(120)

    driver.get(
        "https://the-internet.herokuapp.com/dynamic_loading/2"
        )  # 1. Открыли страницу

    driver.find_element(
        By.CSS_SELECTOR, "#start button"
        ).click()  # 2. Нашли и нажали на кнопку "Start"

    WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.ID, "finish"))
            )  # 3. Дождались появления текста "Hello World!"

    os.makedirs(
        "screenshots", exist_ok=True)  # создали папку, если её нет
    driver.save_screenshot(
        "screenshots/full_screen.png"
        )  # 4. Сделали скриншот страницы

    text = driver.find_element(By.ID, "finish").text
    assert "Hello World!" in text  # 5. Проверка текста (равен "Hello World!")

    driver.quit()
