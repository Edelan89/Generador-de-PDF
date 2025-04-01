import tkinter as tk
from tkinter import ttk
from gui import crear_interfaz
from pdf_generator import crear_pdf


def main_window(splash):  # Recibe splash como argumento
    # Crea la ventana principal
    root = tk.Tk()
    root.title("Formulario de Pacientes")

    # Crear la interfaz gráfica
    fecha_entry, nombre_apellido_entry, edad_entry, sexo_entry, fecha_nacimiento_entry, nacionalidad_entry, ocupacion_entry, estado_civil_entry, dni_entry, cel_fijo_entry, obra_social_entry, afiliado_entry, direccion_entry, comparte_viviendo_entry, familiar_contacto_entry, email_entry, motivo_consulta_entry, tiempo_evolucion_entry, antecedentes_enfermedad_entry, medico_cabecera_entry, elementos_asistencia_entry, estudios_complementarios_entry, cirugias_entry, medicacion_entry, kinesiologia_entry, fonoaudiologia_entry, psicologia_entry, terapia_ocupacional_entry, opiniones_objetivos_entry = crear_interfaz(
        root)

    # Botón para crear el PDF
    def crear_pdf_callback():
        crear_pdf(fecha_entry, nombre_apellido_entry, edad_entry, sexo_entry, fecha_nacimiento_entry, nacionalidad_entry, ocupacion_entry, estado_civil_entry, dni_entry, cel_fijo_entry, obra_social_entry, afiliado_entry, direccion_entry, comparte_viviendo_entry, familiar_contacto_entry, email_entry,
                  motivo_consulta_entry, tiempo_evolucion_entry, antecedentes_enfermedad_entry, medico_cabecera_entry, elementos_asistencia_entry, estudios_complementarios_entry, cirugias_entry, medicacion_entry, kinesiologia_entry, fonoaudiologia_entry, psicologia_entry, terapia_ocupacional_entry, opiniones_objetivos_entry)

    ttk.Button(root, text="Crear PDF", command=crear_pdf_callback).grid(
        row=29, column=0, columnspan=2)

    root.after(0, lambda: splash.destroy())  # Destruye el splash screen
    root.iconbitmap("receta.ico")  # Cambia el icono de la ventana
    root.mainloop()


def splash_screen():
    global splash
    splash = tk.Tk()
    splash.title("Splash Screen")
    splash.overrideredirect(True)  # Oculta la barra de título

    # Configura el tamaño y posición de la ventana
    width = 400
    height = 200
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    splash.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    # Agrega el texto de bienvenida
    texto_bienvenida = "Bienvenido al generador de PDF by Edelan\nMuchas Gracias por Comprar mi Programa <3"
    label = tk.Label(splash, text=texto_bienvenida, font=(
        "Arial", 14), wraplength=350, justify="center")
    label.pack(pady=50)

    # Cierra el splash screen después de 3 segundos y abre la ventana principal
    # Pasa splash como argumento
    splash.after(3000, lambda: main_window(splash))
    splash.mainloop()


if __name__ == "__main__":
    splash_screen()
