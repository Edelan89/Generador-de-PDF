'''Aquí podrías incluir funciones generales que se utilizan en varios lugares del proyecto.'''


def obtener_fecha():
    # Obtener la fecha actual
    from datetime import date
    return date.today().strftime("%d/%m/%Y")
