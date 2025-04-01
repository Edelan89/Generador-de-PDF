import tkinter as tk
from tkinter import ttk


def crear_interfaz(root):
    # Estilo
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 11))
    style.configure("TEntry", font=("Helvetica", 12))

    # Etiquetas y Entradas
    fecha_label = ttk.Label(root, text="Fecha:")
    fecha_label.grid(row=0, column=0, sticky=tk.W)
    fecha_entry = ttk.Entry(root)
    fecha_entry.grid(row=0, column=1)

    nombre_apellido_label = ttk.Label(root, text="Nombre y Apellido:")
    nombre_apellido_label.grid(row=1, column=0, sticky=tk.W)
    nombre_apellido_entry = ttk.Entry(root)
    nombre_apellido_entry.grid(row=1, column=1)

    edad_label = ttk.Label(root, text="Edad:")
    edad_label.grid(row=2, column=0, sticky=tk.W)
    edad_entry = ttk.Entry(root)
    edad_entry.grid(row=2, column=1)

    sexo_label = ttk.Label(root, text="Sexo:")
    sexo_label.grid(row=3, column=0, sticky=tk.W)
    sexo_entry = ttk.Entry(root)
    sexo_entry.grid(row=3, column=1)

    fecha_nacimiento_label = ttk.Label(root, text="Fecha de Nacimiento:")
    fecha_nacimiento_label.grid(row=4, column=0, sticky=tk.W)
    fecha_nacimiento_entry = ttk.Entry(root)
    fecha_nacimiento_entry.grid(row=4, column=1)

    nacionalidad_label = ttk.Label(root, text="Nacionalidad:")
    nacionalidad_label.grid(row=5, column=0, sticky=tk.W)
    nacionalidad_entry = ttk.Entry(root)
    nacionalidad_entry.grid(row=5, column=1)

    ocupacion_label = ttk.Label(root, text="Ocupación:")
    ocupacion_label.grid(row=6, column=0, sticky=tk.W)
    ocupacion_entry = ttk.Entry(root)
    ocupacion_entry.grid(row=6, column=1)

    estado_civil_label = ttk.Label(root, text="Estado Civil:")
    estado_civil_label.grid(row=7, column=0, sticky=tk.W)
    estado_civil_entry = ttk.Entry(root)
    estado_civil_entry.grid(row=7, column=1)

    dni_label = ttk.Label(root, text="DNI:")
    dni_label.grid(row=8, column=0, sticky=tk.W)
    dni_entry = ttk.Entry(root)
    dni_entry.grid(row=8, column=1)

    cel_fijo_label = ttk.Label(root, text="Cel/Fijo:")
    cel_fijo_label.grid(row=9, column=0, sticky=tk.W)
    cel_fijo_entry = ttk.Entry(root)
    cel_fijo_entry.grid(row=9, column=1)

    obra_social_label = ttk.Label(root, text="Obra Social:")
    obra_social_label.grid(row=10, column=0, sticky=tk.W)
    obra_social_entry = ttk.Entry(root)
    obra_social_entry.grid(row=10, column=1)

    afiliado_label = ttk.Label(root, text="Afiliado:")
    afiliado_label.grid(row=11, column=0, sticky=tk.W)
    afiliado_entry = ttk.Entry(root)
    afiliado_entry.grid(row=11, column=1)

    direccion_label = ttk.Label(root, text="Dirección:")
    direccion_label.grid(row=12, column=0, sticky=tk.W)
    direccion_entry = ttk.Entry(root)
    direccion_entry.grid(row=12, column=1)

    comparte_viviendo_label = ttk.Label(root, text="Comparte viviendo con:")
    comparte_viviendo_label.grid(row=13, column=0, sticky=tk.W)
    comparte_viviendo_entry = ttk.Entry(root)
    comparte_viviendo_entry.grid(row=13, column=1)

    familiar_contacto_label = ttk.Label(root, text="Familiar de Contacto:")
    familiar_contacto_label.grid(row=14, column=0, sticky=tk.W)
    familiar_contacto_entry = ttk.Entry(root)
    familiar_contacto_entry.grid(row=14, column=1)

    email_label = ttk.Label(root, text="Email:")
    email_label.grid(row=15, column=0, sticky=tk.W)
    email_entry = ttk.Entry(root)
    email_entry.grid(row=15, column=1)

    motivo_consulta_label = ttk.Label(root, text="Motivo de consulta/Ingreso:")
    motivo_consulta_label.grid(row=16, column=0, sticky=tk.W)
    motivo_consulta_entry = ttk.Entry(root)
    motivo_consulta_entry.grid(row=16, column=1)

    tiempo_evolucion_label = ttk.Label(root, text="Tiempo de Evolución:")
    tiempo_evolucion_label.grid(row=17, column=0, sticky=tk.W)
    tiempo_evolucion_entry = ttk.Entry(root)
    tiempo_evolucion_entry.grid(row=17, column=1)

    antecedentes_enfermedad_label = ttk.Label(
        root, text="Antecedentes de Enfermedad Actual:")
    antecedentes_enfermedad_label.grid(row=18, column=0, sticky=tk.W)
    antecedentes_enfermedad_entry = ttk.Entry(root)
    antecedentes_enfermedad_entry.grid(row=18, column=1)

    medico_cabecera_label = ttk.Label(root, text="Médico de Cabecera:")
    medico_cabecera_label.grid(row=19, column=0, sticky=tk.W)
    medico_cabecera_entry = ttk.Entry(root)
    medico_cabecera_entry.grid(row=19, column=1)

    elementos_asistencia_label = ttk.Label(
        root, text="Elemento de Asistencia:")
    elementos_asistencia_label.grid(row=20, column=0, sticky=tk.W)
    elementos_asistencia_entry = ttk.Entry(root)
    elementos_asistencia_entry.grid(row=20, column=1)

    estudios_complementarios_label = ttk.Label(
        root, text="Estudios Complementarios:")
    estudios_complementarios_label.grid(row=21, column=0, sticky=tk.W)
    estudios_complementarios_entry = ttk.Entry(root)
    estudios_complementarios_entry.grid(row=21, column=1)

    cirugias_label = ttk.Label(root, text="Cirugías:")
    cirugias_label.grid(row=22, column=0, sticky=tk.W)
    cirugias_entry = ttk.Entry(root)
    cirugias_entry.grid(row=22, column=1)

    medicacion_label = ttk.Label(root, text="Medicación:")
    medicacion_label.grid(row=23, column=0, sticky=tk.W)
    medicacion_entry = ttk.Entry(root)
    medicacion_entry.grid(row=23, column=1)

    kinesiologia_label = ttk.Label(root, text="Kinesiología:")
    kinesiologia_label.grid(row=24, column=0, sticky=tk.W)
    kinesiologia_entry = ttk.Entry(root)
    kinesiologia_entry.grid(row=24, column=1)

    fonoaudiologia_label = ttk.Label(root, text="Fonoaudiología:")
    fonoaudiologia_label.grid(row=25, column=0, sticky=tk.W)
    fonoaudiologia_entry = ttk.Entry(root)
    fonoaudiologia_entry.grid(row=25, column=1)

    psicologia_label = ttk.Label(root, text="Psicología:")
    psicologia_label.grid(row=26, column=0, sticky=tk.W)
    psicologia_entry = ttk.Entry(root)
    psicologia_entry.grid(row=26, column=1)

    terapia_ocupacional_label = ttk.Label(root, text="Terapia Ocupacional:")
    terapia_ocupacional_label.grid(row=27, column=0, sticky=tk.W)
    terapia_ocupacional_entry = ttk.Entry(root)
    terapia_ocupacional_entry.grid(row=27, column=1)

    opiniones_objetivos_label = ttk.Label(
        root, text="Opiniones/Objetivos a Trabajar:")
    opiniones_objetivos_label.grid(row=28, column=0, sticky=tk.W)
    opiniones_objetivos_entry = ttk.Entry(root)
    opiniones_objetivos_entry.grid(row=28, column=1)

    return fecha_entry, nombre_apellido_entry, edad_entry, sexo_entry, fecha_nacimiento_entry, nacionalidad_entry, ocupacion_entry, estado_civil_entry, dni_entry, cel_fijo_entry, obra_social_entry, afiliado_entry, direccion_entry, comparte_viviendo_entry, email_entry, familiar_contacto_entry, motivo_consulta_entry, tiempo_evolucion_entry, antecedentes_enfermedad_entry, medico_cabecera_entry, elementos_asistencia_entry, estudios_complementarios_entry, cirugias_entry, medicacion_entry, kinesiologia_entry, fonoaudiologia_entry, psicologia_entry, terapia_ocupacional_entry, opiniones_objetivos_entry
