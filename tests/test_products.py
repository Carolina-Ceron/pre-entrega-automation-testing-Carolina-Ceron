from utils.auxiliar import Auxiliar 
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

def test_products(driver: WebDriver):    
    login_page = Auxiliar(driver)
    login_page.login() 
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == "Products" # Verificar título
    assert driver.find_element(By.ID, 'react-burger-menu-btn').is_displayed()
    assert driver.find_element(By.CLASS_NAME, 'shopping_cart_link').is_displayed()
    assert driver.find_element(By.CLASS_NAME, 'product_sort_container').is_displayed()
    products = login_page.list_products()  # Usamos el método list_products() de Auxiliar
    assert len(products) > 0, "No se encontraron productos en la página de inventario." # Valida presencia de productos
    assert products[0] .find_element(By.CLASS_NAME, 'inventory_item_name').text != "", "El nombre del primer producto está vacío." # Validamos que el nombre no esté vacío
    assert len(products[0].find_element(By.CLASS_NAME, 'inventory_item_price').text)>0 # Validamos que el precio no esté vacío
