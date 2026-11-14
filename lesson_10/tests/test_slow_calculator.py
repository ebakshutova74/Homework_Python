import allure
from selenium import webdriver

from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.title("Медленный калькулятор вычисляет 7+8=15 при задержке 45 секунд")
@allure.description(
    "Проверяем, что при задержке 45 секунд калькулятор корректно "
    "вычисляет 7 + 8 и показывает результат 15."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_shows_15_after_45_seconds() -> None:
    """Проверка вычисления 7+8=15 на калькуляторе с задержкой 45 секунд."""
    driver = webdriver.Chrome()
    try:
        page = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            page.open()

        with allure.step("Установить задержку вычисления 45 секунд"):
            page.set_delay(45)

        with allure.step("Ввести выражение 7 + 8 ="):
            for key in "7+8=":
                page.press(key)

        with allure.step("Дождаться результата и убедиться, что он равен 15"):
            result = page.wait_for_result("15")
            assert result == "15"
    finally:
        driver.quit()
