from selenium import webdriver #Importamos la librería que permite controlar el navegador
import time #Para hacer pausas visibles (solo demo)
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #Creamos la instancia del driver → abre una ventana de Chrome vacía
driver.implicitly_wait(5)
try:
    driver.get('https://www.saucedemo.com') #Navegamos a la URL de Sauce Demo (pantalla de login)
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    assert '/inventory.html' in driver.current_url #Validamos que estamos en el inventario
    assert driver.title == 'Swag Labs' #Validamos que el título sea Swag Labs

    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products' #Validamos que el título de la página sea Products
    assert driver.find_element(By.ID, 'react-burger-menu-btn').is_displayed() #Validamos que el botón de menú esté visible
    assert driver.find_element(By.CLASS_NAME, 'shopping_cart_link').is_displayed() #Validamos que el ícono del carrito esté visible
    assert driver.find_element(By.CLASS_NAME, 'product_sort_container').is_displayed() #Validamos que el combo de ordenamiento esté visible

    productos = driver.find_elements(By.CLASS_NAME,'inventory_item')
    print(f'Cantidad de productos: {len(productos)}') 

    producto_indice = 1
    producto = productos[producto_indice]
    print(
    f"Producto: {producto.find_element(By.CLASS_NAME, 'inventory_item_name').text} - "
    f"Precio: {producto.find_element(By.CLASS_NAME, 'inventory_item_price').text}"
    )
    
    producto.find_element(By.TAG_NAME, 'button').click() #Agregamos al carrito el producto
    assert driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '1' #Validamos que el carrito tenga 1 producto 
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click() #Navegamos al carrito
    assert '/cart.html' in driver.current_url #Validamos que estamos en el carrito
    assert driver.find_element(By.CLASS_NAME, 'cart_item').is_displayed() #Validamos que el producto esté en el carrito

    time.sleep(2)                       #Pausa 
finally:
    driver.quit()                       #Cierre limpio: mata la sesión y la ventana