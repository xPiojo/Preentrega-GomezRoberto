from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver):
    """
    Test automatizado de login en SauceDemo.
    Valida URL, título "Products" y logo "Swag Labs".
    """

    # 1️ Navegar a la página de login
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)  # Espera explícita hasta 10 segundos

    # 2️ Ingresar credenciales válidas
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    # 3️ Validar login exitoso mediante URL
    wait.until(EC.url_contains("/inventory.html"))
    assert driver.current_url.endswith("/inventory.html"), "❌ El login falló o no redirigió correctamente."

    # 4️ Validar presencia del título "Products"
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "title"), "Products"))

    # 5️ Validar presencia del logo "Swag Labs"
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "app_logo"), "Swag Labs"))

    print("✅ Login exitoso y validaciones correctas.")
