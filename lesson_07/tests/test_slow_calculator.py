from selenium import webdriver

from pages.calculator_page import CalculatorPage


def test_calculator_shows_15_after_45_seconds():
    driver = webdriver.Chrome()
    try:
        page = CalculatorPage(driver)

        # 1. Открыть страницу калькулятора
        page.open()

        # 2. Ввести значение 45 в поле задержки
        page.set_delay(45)

        # 3. Нажать кнопки: 7, +, 8, =
        for key in "7+8=":
            page.press(key)

        # 4. Проверить, что через 45 секунд на экране появится 15
        result = page.wait_for_result("15")
        assert result == "15"

    finally:
        driver.quit()
