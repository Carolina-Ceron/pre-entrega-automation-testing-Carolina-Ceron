from selenium.webdriver.common.by import By 
from selenium.webdriver.remote.webdriver import WebDriver

class Auxiliar:
    def __init__(self, driver: WebDriver):
        self.driver = driver # El driver viene de conftest.py
        self.URL = "https://www.saucedemo.com/"
        self.USERNAME_FIELD = (By.ID, "user-name")
        self.PASSWORD_FIELD = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login-button")
        self.username = "standard_user"
        self.password = "secret_sauce"

    def login(self):
        # La apertura de la página se hace en el método de login
        self.driver.get(self.URL)
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(self.username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(self.password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def list_products(self):
        return self.driver.find_elements(By.CLASS_NAME, 'inventory_item')