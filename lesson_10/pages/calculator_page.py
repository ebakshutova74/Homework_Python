from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object страницы медленного калькулятора (slow-calculator.html)."""

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver) -> None:
        """Сохраняет драйвер для работы со страницей калькулятора."""
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу калькулятора в браузере."""
        self.driver.get(self.URL)

    def set_delay(self, seconds: int) -> None:
        """Задаёт задержку вычисления в секундах."""
        field = self.driver.find_element(*self.DELAY_INPUT)
        field.clear()
        field.send_keys(str(seconds))

    def press(self, key: str) -> None:
        """Нажимает кнопку калькулятора по её подписи (цифра, знак или '=')."""
        button = self.driver.find_element(
            By.XPATH, f"//span[normalize-space(text())='{key}']"
        )
        button.click()

    def wait_for_result(self, expected: str) -> str:
        """Ждёт появления ожидаемого значения на экране и возвращает текст экрана."""
        screen = self.driver.find_element(*self.SCREEN)
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )
        return screen.text
