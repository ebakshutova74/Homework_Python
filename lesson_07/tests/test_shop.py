from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_purchase_flow():
    driver = webdriver.Firefox()
    try:
        # 1. Открыть сайт и авторизоваться
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        # 2. Добавить три товара
        inventory = InventoryPage(driver)
        inventory.add_to_cart("sauce-labs-backpack")
        inventory.add_to_cart("sauce-labs-bolt-t-shirt")
        inventory.add_to_cart("sauce-labs-onesie")

        # 3. Перейти в корзину и проверить её содержимое
        inventory.go_to_cart()
        cart = CartPage(driver)
        items = cart.get_item_names()
        assert "Sauce Labs Backpack" in items
        assert "Sauce Labs Bolt T-Shirt" in items
        assert "Sauce Labs Onesie" in items

        # 4. Checkout и заполнение формы
        cart.checkout()
        checkout = CheckoutPage(driver)
        checkout.fill_form("Имя", "Фамилия", "620000")
        checkout.click_continue()

        # 5. Прочитать итоговую сумму
        total = checkout.get_total()
    finally:
        # 6. Закрыть браузер — до assert, как в задании
        driver.quit()

    # 7. Проверка суммы после закрытия браузера
    assert total == "$58.29"
