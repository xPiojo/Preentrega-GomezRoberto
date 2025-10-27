from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_inventory_page(driver):
    """
    Test de navegación y verificación del catálogo en SauceDemo:
    - Verifica título de la página de inventario
    - Comprueba que haya productos visibles
    - Valida elementos de la interfaz (menú, filtros)
    - Lista nombre y precio del primer producto
    """

    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    # 1️ Login previo
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    wait.until(EC.url_contains("/inventory.html"))

    # 2️ Validar título de la página
    assert driver.title == "Swag Labs", "❌ El título de la página no coincide."

    # 3️ Comprobar que hay productos visibles
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "❌ No hay productos visibles en la página."

    # 4️ Validar elementos importantes de la interfaz
    menu_icon = wait.until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
    filtro_dropdown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))

    assert menu_icon.is_displayed(), "❌ El menú no está visible."
    assert filtro_dropdown.is_displayed(), "❌ El filtro de productos no está visible."

    # 5️ Listar nombre y precio del primer producto
    primer_producto = productos[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"✅ Primer producto: {nombre} - Precio: {precio}")
