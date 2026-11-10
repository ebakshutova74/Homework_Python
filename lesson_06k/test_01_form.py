from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )

        # Ждем появления первого поля, чтобы страница точно прогрузилась
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "first-name"))
        )

        # Заполняем поля (можно оставить как у тебя или использовать цикл)
        data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "zip-code": "",  # Специально пустая строка
            "city": "Москва",
            "country": "Россия",
            "e-mail": "test@skypro.com",
            "phone": "+79858999987",
            "job-position": "QA",
            "company": "SkyPro",
        }

        for name, value in data.items():
            field = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.NAME, name))
            )
            field.send_keys(value)

        # Находим и жмем кнопку Submit
        submit_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Submit')]"))
        )
        submit_button.click()

        # Ждем, пока появится блок ошибки для zip-code.
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.alert-danger#zip-code"))
        )

        # 1. Проверка, что zip-code подсвечен красным
        red_alert = driver.find_element(
            By.CSS_SELECTOR, "div.alert-danger#zip-code")
        assert red_alert.is_displayed(), (
            "Блок ошибки для zip-code не появился!")

        # 2. Проверка, что остальные поля подсвечены зеленым
        # Проверим, что для каждого поля есть свой зеленый блок.
        expected_green_fields = [
            "first-name", "last-name", "address", "city",
            "country", "e-mail", "phone", "job-position", "company"
        ]

        for field_name in expected_green_fields:
            # Ищем div с классом success и ID, равным имени поля
            selector = f"div.alert-success#{field_name}"
            try:
                green_block = driver.find_element(By.CSS_SELECTOR, selector)
                assert green_block.is_displayed(), (
                    f"Нет зеленого блока для поля {field_name}")
            except Exception:
                # Если блок не найден, выводим ошибку и прерываем тест
                raise AssertionError(
                    f"Не найден зеленый блок валидации для поля: {field_name}")

    finally:
        driver.quit()
