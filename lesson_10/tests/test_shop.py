import allure
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Магазин")
@allure.title(
    "Полный цикл покупки: логин, три товара, корзина, checkout и сумма")
@allure.description(
    "Проверяем сквозной сценарий магазина Sauce Demo: авторизация, "
    "добавление трёх товаров в корзину, оформление заказа и "
    "итоговая сумма $58.29."
)
@allure.severity(allure.severity_level.BLOCKER)
def test_shop_purchase_flow() -> None:
    """Сквозной тест покупки трёх товаров с проверкой итоговой суммы."""
    driver = webdriver.Firefox()
    try:
        with allure.step("Открыть сайт и авторизоваться"):
            login = LoginPage(driver)
            login.open()
            login.login("standard_user", "secret_sauce")

        with allure.step("Добавить три товара в корзину"):
            inventory = InventoryPage(driver)
            inventory.add_to_cart("sauce-labs-backpack")
            inventory.add_to_cart("sauce-labs-bolt-t-shirt")
            inventory.add_to_cart("sauce-labs-onesie")

        with allure.step("Перейти в корзину и проверить её содержимое"):
            inventory.go_to_cart()
            cart = CartPage(driver)
            items = cart.get_item_names()
            assert "Sauce Labs Backpack" in items
            assert "Sauce Labs Bolt T-Shirt" in items
            assert "Sauce Labs Onesie" in items

        with allure.step("Заполнить форму checkout и перейти к обзору заказа"):
            cart.checkout()
            checkout = CheckoutPage(driver)
            checkout.fill_form("Имя", "Фамилия", "620000")
            checkout.click_continue()

        with allure.step("Прочитать итоговую сумму заказа"):
            total = checkout.get_total()
    finally:
        with allure.step("Закрыть браузер до проверки суммы"):
            driver.quit()

    with allure.step("Убедиться, что итоговая сумма равна $58.29"):
        assert total == "$58.29"
