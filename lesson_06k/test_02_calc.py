from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    # В поле по локатору #delay вводим значение 45
    delay_field = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_field.clear()
    delay_field.send_keys("45")

    # Нажимаем 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ждём результат до 45+ секунд
    screen = (By.CSS_SELECTOR, ".screen")
    WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element(screen, "15")
        )

    result = driver.find_element(By.CSS_SELECTOR, ".screen")
    assert result.text.strip() == "15", (
            f"Ожидали '15', получено: '{result.text}'"
        )

    driver.quit()
