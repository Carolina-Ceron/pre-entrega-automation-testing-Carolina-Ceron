Pre-Entrega Proyecto: Automatización QA - Saucedemo

## Propósito del Proyecto

Este proyecto representa la pre-entrega de la asignatura de Automatización QA. 
El objetivo principal es aplicar los conocimientos adquiridos hasta la Clase 8 del curso para demostrar la capacidad de automatizar flujos básicos de navegación web utilizando el sitio de práctica www.saucedemo.com.


Se automatizaron y validaron las siguientes funcionalidades:

* **Login Exitoso:** Ingreso con credenciales válidas (`standard_user` / `secret_sauce`) y validación de la redirección a la página de inventario (`/inventory.html`).
* **Verificación del Catálogo:** Validación del título de la página (`Products/Swag Labs`), y verificación de la presencia de elementos importantes de la interfaz (menú, filtros).
* **Presencia de Productos:** Comprobación de que existen productos visibles en la página y listado del nombre/precio del primer producto.
* **Interacción con Carrito (Add to Cart):** Caso de prueba para agregar un producto al carrito y validar la correcta actualización del contador.

## Tecnologías Utilizadas

El proyecto fue desarrollado utilizando el siguiente stack tecnológico:
| Herramienta | Función |
| :--- | :--- |
| **Python** | Lenguaje de programación principal. |
| **Pytest** | Framework para la estructura de testing. |
| **Selenium WebDriver** | Biblioteca para la automatización web. |
| **Git & GitHub** | Control de versiones y repositorio de código. |
| **`pytest-html`** | Plugin para la generación de reportes. |

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium%20WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)


## Instrucciones de Instalación de Dependencias

Para ejecutar este proyecto, es necesario tener instalado Python. 

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Carolina-Ceron/pre-entrega-automation-testing-Carolina-Ceron.git
    ```


2.  **Instalar dependencias:**
    Asegúrate de que el archivo `requirements.txt` esté presente en la raíz del proyecto.
    ```bash
    pip install -r requirements.txt
    ```
    *Nota: Este comando instalará `selenium`, `pytest`, y `pytest-html`.*

---



## Instrucciones para ejecutar las pruebas y generar reporte HTML:
```bash
pytest -v --html reports/reporte.html
```

Una vez finalizada la ejecución, el archivo reporte.html estará disponible para su revisión.

