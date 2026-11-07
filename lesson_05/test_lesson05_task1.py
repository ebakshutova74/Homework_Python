from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.qa-territory.online")  # Открываем страницу

    print("Страница открыта")

    element = driver.find_element(By.LINK_TEXT, "HTML Form")
    element.click()  # Находим и кликаем на ссылку HTML Form

    # Проверяем, что URL изменился на /forms/post
    assert "/forms/post" in driver.current_url

    print("URL:", driver.current_url)

# Возвращаемся на главную страницу
    driver.back()

# Проверяем, что вернулись на исходный URL
    assert driver.current_url == "https://httpbin.qa-territory.online"


# Закрываем браузер
    driver.quit()
