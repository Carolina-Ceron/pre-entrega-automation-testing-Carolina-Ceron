import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function") #Maneja el ciclo de vida del WebDriver
def driver(): # Setup del Driver con opciones personalizadas
    chrome_options = Options()
    chrome_options.add_argument("--guest") 
    chrome_options.add_argument("--disable-extensions") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-save-password-bubble") 
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options) 
    driver.implicitly_wait(5)
        # El test se ejecuta aquí
    yield driver
    driver.quit() # Teardown: Cerrar el driver al finalizar el test