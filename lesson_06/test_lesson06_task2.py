from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


COOKIE_NAME = "SESSION"
COOKIE_VALUE_1 = "NWFkOGIxNzItYzJjMi00MjMxLTg1NzctYmQyNmJlZDczMDQ0"
COOKIE_VALUE_2 = "MjZmNjU1ZmEtNDM1NC00NmE5LTk1NDAtZmJjYzViYmFiYjg5"

LOGIN_USER_1 = "Zibaga"
LOGIN_USER_2 = "Bakelval"


def test_two_users():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://gitflic.ru/")  # Открыли страницу

    driver.add_cookie(
        {"name": COOKIE_NAME, "value": COOKIE_VALUE_1}
        )  # Вводим данные 1 пользователя

    driver.refresh()
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
        )  # Обновили страницу

    driver.get(
        f"https://gitflic.ru/user/{LOGIN_USER_1}"
        )  # Перешли на страницу пользователя 1

    url_user1 = driver.current_url
    print(url_user1)  # Сохранили текущий URL

    driver.delete_all_cookies()  # очистили куки

    driver.add_cookie(
        {"name": COOKIE_NAME, "value": COOKIE_VALUE_2}
        )  # Установили данные пользователя 2

    driver.refresh()
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
        )  # Обновили страницу

    driver.get(
        f"https://gitflic.ru/user/{LOGIN_USER_2}"
        )  # Перешли на страницу пользователя 2

    url_user2 = driver.current_url
    print(url_user2)  # Сохранили текущий URL

    assert url_user1 != url_user2, (
        f"URL совпадают: {url_user1}"
    )  # Проверяем, что URL для пользователей 1 и 2 различаются

    driver.quit()
