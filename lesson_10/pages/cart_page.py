from selenium.webdriver.common.by import By


class CartPage:
    """Page Object страницы корзины Sauce Demo."""

    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '[data-test="checkout"]')

    def __init__(self, driver) -> None:
        """Сохраняет драйвер для работы со страницей корзины."""
        self.driver = driver

    def get_item_names(self) -> list[str]:
        """Возвращает список названий товаров в корзине."""
        return [
            item.text for item in self.driver.find_elements(*self.ITEM_NAMES)
        ]

    def checkout(self) -> None:
        """Нажимает кнопку перехода к оформлению заказа."""
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
