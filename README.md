# Pre-Entrega Automation Testing - Roberto Gomez

## Propósito del proyecto
Este proyecto automatiza pruebas de QA sobre la página [saucedemo.com](https://www.saucedemo.com/) para validar funcionalidades de login, catálogo de productos y carrito de compras.

## Tecnologías utilizadas
- Python 3.x
- Selenium
- Pytest
- Chrome WebDriver
- pytest-html (para reportes en HTML)

## Instalación de dependencias
1. Crear un entorno virtual (opcional pero recomendado):
    ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

2. Instalar dependencias:

    ```bash
    Copiar código
    pip install -r requirements.txt

## Cómo ejecutar las pruebas

Para correr todos los tests y generar un reporte HTML:
    ```bash
    pytest -v --html=reports/reporte.html


Los tests se ejecutan de manera independiente.

Se utilizan fixtures para manejar el navegador y capturas automáticas de fallos.

## Estructura del proyecto

tests/ → Contiene todos los tests automatizados.

reports/ → Reportes HTML y capturas de pantalla en caso de fallos.

conftest.py → Fixture de pytest y hooks para screenshots automáticos.

## Evidencias adicionales

Capturas de pantalla automáticas en caso de fallos.

Reportes HTML generados automáticamente en reports/reporte.html.
