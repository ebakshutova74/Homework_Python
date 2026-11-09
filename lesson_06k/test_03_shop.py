from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Firefox()

    try:
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Дожидаемся каталога товаров
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "inventory_container"))
        )

        # Добавляем три товара в корзину
        items = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie",
        ]
        for item_id in items:
            driver.find_element(By.ID, item_id).click()

        # Переходим в корзину
        driver.find_element(By.ID, "shopping_cart_container").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "cart_contents_container"))
        )

        # Checkout
        driver.find_element(By.ID, "checkout").click()

        # Заполняем форму
        driver.find_element(By.ID, "first-name").send_keys("Марина")
        driver.find_element(By.ID, "last-name").send_keys("Мнишек")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        # Ждём страницу итоговой стоимости и читаем Total
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "checkout_summary_container"))
        )
        total_text = driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        ).text

        # Закрываем браузер
    finally:
        driver.quit()

    # Проверяем итоговую сумму
    assert "$58.29" in total_text, (
        f"Ожидали '$58.29', получено: '{total_text}'"
    )
