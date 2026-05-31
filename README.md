<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
</p>

<h1 align="center">MATRÍCULAS</h1>

<p align="center">
  <strong>🌐 <a href="https://curroayala.pythonanywhere.com/">Jugar ahora</a></strong>
</p>

## 📖 Descripción

**Matrículas** es un minijuego web interactivo que consiste en proporcionar una palabra a partir de tres letras aleatorias, simulando el clásico pasatiempo de adivinar palabras con las letras de las matrículas de los coches.

### 📜 Reglas del Juego
Una palabra se considera válida si, y solo si, cumple estas tres condiciones:
1. **Contiene las letras:** Debe incluir las tres letras de la matrícula proporcionada.
2. **Orden correcto:** Las letras deben aparecer en la palabra en el mismo orden que en la matrícula.
3. **Diccionario:** La palabra tiene que existir en el idioma español.

## 🛠️ Stack Tecnológico

Este proyecto ha sido construido utilizando las siguientes herramientas y tecnologías:

* **Backend:** [Python](https://www.python.org/) y el framework web [Django](https://www.djangoproject.com/) (v6.0.5).
* **Base de datos:** [SQLite](https://www.sqlite.org/), para el registro de usuarios y el guardado de las estadísticas.
* **Frontend:** HTML5, CSS3 (arquitectura *Mobile-First*, Flexbox/Grid y variables CSS) y *Django Templates* para el renderizado dinámico de las vistas.
* **Validación:** Uso de la librería `pyspellchecker` para verificar que la palabra introducida por el usuario sea real y exista en español.
