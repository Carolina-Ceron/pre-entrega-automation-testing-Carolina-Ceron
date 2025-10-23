from utils.auxiliar import Auxiliar 
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_exitoso(driver: WebDriver): 
    login_page = Auxiliar(driver)
    login_page.login()
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )
    assert "inventory.html" in driver.current_url
    assert driver.title == "Swag Labs" 