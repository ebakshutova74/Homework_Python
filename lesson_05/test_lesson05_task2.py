from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    driver.get(
        "https://httpbin.qa-territory.online/forms/post"
        )  # Открываем страницу

    name_input = driver.find_element(
        By.NAME, "custname")  # Ищем поле ввода по локатору name

    name_input.send_keys("Elena")  # Вводим имя

    submit_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Submit')]")

    submit_button.click()  # Находим кнопку Submit и кликаем

    expected_url = "https://httpbin.qa-territory.online/forms/post"

    assert driver.current_url == expected_url  # Проверяем, изменился ли URL

    print("URL изменился")

    driver.quit()
