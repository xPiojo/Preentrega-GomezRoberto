from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_agregar_producto_al_carrito(driver):
    """
    Test de carrito en SauceDemo:
    - Añade el primer producto al carrito
    - Verifica contador del carrito
    - Comprueba que el producto aparece en el carrito
    """

    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    # 1️ Login previo
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    wait.until(EC.url_contains("/inventory.html"))

    # 2️ Tomar el nombre del primer producto antes de agregarlo
    primer_producto = driver.find_element(By.CSS_SELECTOR, ".inventory_item:first-child")
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    # 3️ Añadir el producto al carrito
    primer_producto.find_element(By.TAG_NAME, "button").click()

    # 4️ Verificar que el contador del carrito se incrementó a 1
    assert wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1")
    ), "❌ El contador del carrito no se incrementó correctamente."

    # 5️ Navegar al carrito
    carrito_icono = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    carrito_icono.click()
    wait.until(EC.url_contains("/cart.html"))

    # 6️ Verificar que el producto aparezca en el carrito
    producto_en_carrito = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//div[@class='inventory_item_name' and text()='{nombre_producto}']")
        )
    )
    assert producto_en_carrito.is_displayed(), "❌ El producto añadido no aparece en el carrito."


    print("✅ Producto agregado y verificado correctamente en el carrito.")
