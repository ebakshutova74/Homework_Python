from selenium.webdriver.common.by import By


class CartPage:
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '[data-test="checkout"]')

    def __init__(self, driver):
        self.driver = driver

    def get_item_names(self):
        return [
            item.text for item in self.driver.find_elements(*self.ITEM_NAMES)
        ]

    def checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
