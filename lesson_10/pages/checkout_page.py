from selenium.webdriver.common.by import By


class CheckoutPage:
    """Page Object страницы оформления заказа Sauce Demo."""

    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[data-test="continue"]')
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver) -> None:
        """Сохраняет драйвер для работы со страницей оформления заказа."""
        self.driver = driver

    def fill_form(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """Заполняет форму данными покупателя."""
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self) -> None:
        """Нажимает кнопку Continue и переходит к обзору заказа."""
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total(self) -> str:
        """Возвращает сумму заказа строкой без подписи 'Total: ' и '$'."""
        text = self.driver.find_element(*self.TOTAL).text
        # Из "Total: $58.29" достаём только сумму
        return text.split(":")[1].strip()
