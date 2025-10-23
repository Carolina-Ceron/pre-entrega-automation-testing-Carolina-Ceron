from utils.auxiliar import Auxiliar 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.remote.webdriver import WebDriver

def test_add_cart(driver: WebDriver): # ⬅️ ACEPTA LA FIXTURE 'driver'
    login_page = Auxiliar(driver)
    login_page.login() # Necesario: Inicia sesión
    cart_elements = driver.find_elements(By.CLASS_NAME, 'shopping_cart_badge')
    if len(cart_elements) > 0:
        current_cart_count = int(cart_elements[0].text)
    else:
        current_cart_count = 0
    all_products = login_page.list_products() # Usar el método POM para obtener la lista de productos
    if not all_products:
        raise Exception("No se encontraron productos para agregar al carrito.")
    first_product = all_products[0]
    first_product.find_element(By.TAG_NAME, 'button').click()
    try:
        wait = WebDriverWait(driver, 10)
        new_cart_element = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))
        )
        new_cart_count = int(new_cart_element.text) # Leemos el nuevo valor
    except Exception: # Si el contador no aparece, fallamos con un valor que hará fallar el assert
        print("Error: El contador del carrito no apareció/actualizó después de 10s.")
        new_cart_count = -1 
    assert new_cart_count == current_cart_count + 1, \
        f"Error: Se esperaban {current_cart_count + 1} productos, pero se obtuvo {new_cart_count}."