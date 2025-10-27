import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture
def driver():
    # Setup: se ejecuta antes del test
    chrome_opt = Options()
    chrome_opt.add_argument("--incognito")
    # Si querés que no abra la ventana del navegador, descomentá la siguiente línea:
    # chrome_opt.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_opt)
    driver.maximize_window()

    yield driver  # 🔹 Entrega el driver al test

    # Teardown: se ejecuta después del test
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest: se ejecuta después de cada test.
    Si el test falla, toma una captura de pantalla y la guarda en /screenshots.
    """
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            print(f"\n📸 Captura guardada en: {screenshot_path}")
