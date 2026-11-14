from selenium.webdriver.common.by import By


class InventoryPage:
    """Page Object страницы каталога товаров Sauce Demo."""

    CART_LINK = (By.CSS_SELECTOR, "#shopping_cart_container a")

    def __init__(self, driver) -> None:
        """Сохраняет драйвер для работы со страницей каталога."""
        self.driver = driver

    def add_to_cart(self, item_slug: str) -> None:
        """Кликает по кнопке добавления товара в корзину по его slug-идентификатору."""
        button = self.driver.find_element(
            By.CSS_SELECTOR, f'[data-test="add-to-cart-{item_slug}"]'
        )
        button.click()

    def go_to_cart(self) -> None:
        """Переходит в корзину по ссылке в шапке страницы."""
        self.driver.find_element(*self.CART_LINK).click()
