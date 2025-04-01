Generador de PDF para Formulario de Pacientes
Este proyecto es una aplicación de escritorio desarrollada en Python que permite a los usuarios llenar un formulario de pacientes y generar un archivo PDF con la información ingresada. Utiliza bibliotecas como tkinter para la interfaz gráfica y reportlab para la generación de PDFs.

Características
Interfaz gráfica amigable para ingresar datos del paciente.

Generación automática de un archivo PDF con el contenido del formulario.

Posibilidad de personalizar el nombre y ubicación del archivo generado.

Pantalla de bienvenida (Splash Screen) al iniciar la aplicación.

Requisitos del sistema
Python 3.8 o superior.

Bibliotecas necesarias:

tkinter (incluida en Python por defecto).

reportlab.

Instalación
Clona este repositorio o descarga los archivos del proyecto.

Asegúrate de tener instaladas las dependencias necesarias ejecutando:

bash
pip install reportlab
Ejecuta el archivo principal:

bash
python main.py
Estructura del proyecto
El proyecto está dividido en varios módulos para facilitar su mantenimiento:

Archivo	Descripción
main.py	Archivo principal que inicia la aplicación y gestiona el flujo general.
gui.py	Define la interfaz gráfica utilizando tkinter.
pdf_generator.py	Contiene la lógica para generar el archivo PDF con los datos ingresados.
utils.py	Funciones auxiliares, como obtener la fecha actual.
Cómo usar
Ejecuta el programa con:

bash
python main.py
Completa los campos del formulario en la ventana principal.

Haz clic en el botón "Crear PDF".

Selecciona una ubicación para guardar el archivo PDF generado.

Notas técnicas
1. Interfaz gráfica (gui.py)
La interfaz gráfica incluye:

Campos de entrada organizados por categorías (datos personales, contacto, antecedentes médicos, etc.).

Botón para generar el PDF.

2. Generación del PDF (pdf_generator.py)
El módulo utiliza reportlab para crear un documento PDF con:

Títulos y subtítulos formateados.

Información organizada en secciones.

3. Pantalla de bienvenida (main.py)
Al iniciar, se muestra un Splash Screen con un mensaje de bienvenida antes de abrir la ventana principal.

Contribución
Si deseas mejorar este proyecto:

Haz un fork del repositorio.

Crea una nueva rama:

bash
git checkout -b feature/nueva-funcionalidad
Realiza tus cambios y envía un pull request.

Autor
Este programa fue desarrollado por Edelan como una solución para gestionar formularios y generar reportes en formato PDF.

¡Gracias por usar este programa! 😊