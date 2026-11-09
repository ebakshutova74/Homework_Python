from selenium.webdriver.common.by import By


class InventoryPage:
    CART_LINK = (By.CSS_SELECTOR, "#shopping_cart_container a")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_slug):
        button = self.driver.find_element(
            By.CSS_SELECTOR, f'[data-test="add-to-cart-{item_slug}"]'
        )
        button.click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
