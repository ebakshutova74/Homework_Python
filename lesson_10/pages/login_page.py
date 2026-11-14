from selenium.webdriver.common.by import By


class LoginPage:
    """Page Object страницы логина Sauce Demo."""

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

    def __init__(self, driver) -> None:
        """Сохраняет драйвер и локаторы для работы со страницей логина."""
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу логина в браузере."""
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        """Вводит логин и пароль и нажимает кнопку входа."""
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
