"""Este módulo se encargará de generar el PDF."""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
import tkinter as tk
from tkinter import filedialog


def crear_pdf(fecha_entry, nombre_apellido_entry, edad_entry, sexo_entry, fecha_nacimiento_entry, nacionalidad_entry, ocupacion_entry, estado_civil_entry, dni_entry, cel_fijo_entry, obra_social_entry, afiliado_entry, direccion_entry, comparte_viviendo_entry, familiar_contacto_entry, email_entry,  motivo_consulta_entry, tiempo_evolucion_entry, antecedentes_enfermedad_entry, medico_cabecera_entry, elementos_asistencia_entry, estudios_complementarios_entry, cirugias_entry, medicacion_entry, kinesiologia_entry, fonoaudiologia_entry, psicologia_entry, terapia_ocupacional_entry, opiniones_objetivos_entry):

    # Obtener los valores de las entradas
    fecha = fecha_entry.get()
    nombre_apellido = nombre_apellido_entry.get()
    edad = edad_entry.get()
    sexo = sexo_entry.get()
    fecha_nacimiento = fecha_nacimiento_entry.get()
    nacionalidad = nacionalidad_entry.get()
    ocupacion = ocupacion_entry.get()
    estado_civil = estado_civil_entry.get()
    dni = dni_entry.get()
    cel_fijo = cel_fijo_entry.get()
    obra_social = obra_social_entry.get()
    afiliado = afiliado_entry.get()
    direccion = direccion_entry.get()
    comparte_viviendo = comparte_viviendo_entry.get()
    familiar_contacto = familiar_contacto_entry.get()
    email = email_entry.get()
    motivo_consulta = motivo_consulta_entry.get()
    tiempo_evolucion = tiempo_evolucion_entry.get()
    antecedentes_enfermedad = antecedentes_enfermedad_entry.get()
    medico_cabecera = medico_cabecera_entry.get()
    elementos_asistencia = elementos_asistencia_entry.get()
    estudios_complementarios = estudios_complementarios_entry.get()
    cirugias = cirugias_entry.get()
    medicacion = medicacion_entry.get()
    kinesiologia = kinesiologia_entry.get()
    fonoaudiologia = fonoaudiologia_entry.get()
    psicologia = psicologia_entry.get()
    terapia_ocupacional = terapia_ocupacional_entry.get()
    opiniones_objetivos = opiniones_objetivos_entry.get()

    # Abrir archivo de dialogo para seleccionar carpeta de guardado
    nombre_archivo = filedialog.asksaveasfilename(initialdir="/", title="Guardar PDF", defaultextension=".pdf", filetypes=[
        ("PDF Files", "*.pdf")], initialfile=f"{nombre_apellido}.pdf")

    if nombre_archivo:
        # Generar el pdf en la carpeta seleccionada
        try:
            c = canvas.Canvas(nombre_archivo, pagesize=letter)
            c.setFont('Helvetica', 10)
            x, y = inch, 10.5 * inch
            dy = 0.25 * inch

            styles = getSampleStyleSheet()
            styleN = styles['Normal']
            styleN.alignment = TA_LEFT
            styleN.fontSize = 10
            styleH = styles['Normal']
            styleH.fontName = 'Helvetica-Bold'
            styleH.alignment = TA_LEFT
            styleH.fontSize = 12
            styleT = styles['Heading1']
            styleT.alignment = TA_CENTER
            styleT.fontSize = 16
            styleT.fontName = 'Helvetica-Bold'

            # Títulos
            titulo = Paragraph("Neurorehabilitación", styleT)
            w, h = titulo.wrapOn(c, letter[0] - 2 * inch, letter[1])
            titulo.drawOn(c, inch, y - h)
            y -= h + dy * 2

            c.setFont('Helvetica', 11)
            c.drawString(x, y, "Fecha:")
            c.drawString(x + 0.7 * inch, y, fecha)
            y -= dy * 2

            subtitulo = Paragraph("Evaluación de Ingreso", styleT)
            w, h = subtitulo.wrapOn(c, letter[0] - 2 * inch, letter[1])
            subtitulo.drawOn(c, inch, y - h)
            y -= h + dy * 2

            data = [
                ("Nombre y Apellido:", nombre_apellido),
                ("Edad:", edad),
                ("Sexo:", sexo),
                ("Fecha de Nacimiento:", fecha_nacimiento),
                ("Nacionalidad:", nacionalidad),
                ("Ocupación:", ocupacion),
                ("Estado Civil:", estado_civil),
                ("DNI:", dni),
                ("Cel/Fijo:", cel_fijo),
                ("Obra Social:", obra_social),
                ("Afiliado:", afiliado),
                ("Dirección:", direccion),
                ("Comparte Viviendo Con:", comparte_viviendo),
                ("Familiar de Contacto:", familiar_contacto),
                ("Email:", email),
                ("Motivo de Consulta/Ingreso:", motivo_consulta),
                ("Tiempo de Evolución:", tiempo_evolucion),
                ("Antecedentes de Enfermedad Actual:", antecedentes_enfermedad),
                ("Médico de Cabecera:", medico_cabecera),
                ("Elemento de Asistencia:", elementos_asistencia),
                ("Estudios Complementarios:", estudios_complementarios),
                ("Cirugías:", cirugias),
                ("Medicación:", medicacion),
            ]

            for tag, content in data:
                tag_paragraph = Paragraph(f"{tag}", styles['Normal'])
                w, h = tag_paragraph.wrapOn(c, letter[0] - 2 * inch, letter[1])
                if y - h < inch:
                    c.showPage()
                    y = 10.5 * inch
                tag_paragraph.drawOn(c, inch, y - h)
                y -= h

                content_paragraph = Paragraph(content, styles['Normal'])
                w, h = content_paragraph.wrapOn(
                    c, letter[0] - 2 * inch, letter[1])
                if y - h < inch:
                    c.showPage()
                    y = 10.5 * inch
                content_paragraph.drawOn(c, inch, y - h)
                y -= h + dy * 2

            propuesta_titulo = Paragraph(
                "Propuesta Terapéutica / Áreas de Neurorehabilitación", styleT)
            w, h = propuesta_titulo.wrapOn(c, letter[0] - 2 * inch, letter[1])
            if y - h < inch:
                c.showPage()
                y = 10.5 * inch
            propuesta_titulo.drawOn(c, inch, y - h)
            y -= h + dy * 2

            terapias = [
                ("Kinesiología:", kinesiologia),
                ("Fonoaudiología:", fonoaudiologia),
                ("Psicología:", psicologia),
                ("Terapia Ocupacional:", terapia_ocupacional),
                ("Opiniones/Objetivos a Trabajar:", opiniones_objetivos),
            ]

            for tag, content in terapias:
                tag_paragraph = Paragraph(f"{tag}", styles['Normal'])
                w, h = tag_paragraph.wrapOn(c, letter[0] - 2 * inch, letter[1])
                if y - h < inch:
                    c.showPage()
                    y = 10.5 * inch
                tag_paragraph.drawOn(c, inch, y - h)
                y -= h

                content_paragraph = Paragraph(content, styles['Normal'])
                w, h = content_paragraph.wrapOn(
                    c, letter[0] - 2 * inch, letter[1])
                if y - h < inch:
                    c.showPage()
                    y = 10.5 * inch
                content_paragraph.drawOn(c, inch, y - h)
                y -= h + dy * 2

            c.save()
            print(f"PDF guardado en: {nombre_archivo}")

        except Exception as e:
            print(f"Error al guardar el PDF: {e}")
    else:
        print("No se selecciono una ubicacion de guardado.")

    # Borrar los datos de los Entry
    fecha_entry.delete(0, tk.END)
    nombre_apellido_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    sexo_entry.delete(0, tk.END)
    fecha_nacimiento_entry.delete(0, tk.END)
    nacionalidad_entry.delete(0, tk.END)
    ocupacion_entry.delete(0, tk.END)
    estado_civil_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    cel_fijo_entry.delete(0, tk.END)
    obra_social_entry.delete(0, tk.END)
    afiliado_entry.delete(0, tk.END)
    direccion_entry.delete(0, tk.END)
    comparte_viviendo_entry.delete(0, tk.END)
    familiar_contacto_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    motivo_consulta_entry.delete(0, tk.END)
    tiempo_evolucion_entry.delete(0, tk.END)
    antecedentes_enfermedad_entry.delete(0, tk.END)
    medico_cabecera_entry.delete(0, tk.END)
    elementos_asistencia_entry.delete(0, tk.END)
    estudios_complementarios_entry.delete(0, tk.END)
    cirugias_entry.delete(0, tk.END)
    medicacion_entry.delete(0, tk.END)
    kinesiologia_entry.delete(0, tk.END)
    fonoaudiologia_entry.delete(0, tk.END)
    psicologia_entry.delete(0, tk.END)
    terapia_ocupacional_entry.delete(0, tk.END)
    opiniones_objetivos_entry.delete(0, tk.END)
