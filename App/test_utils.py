from utils import obtener_fecha
from datetime import date


def test_obtener_fecha():
    # Obtener la fecha actual en formato dd/mm/yyyy
    fecha_actual = date.today().strftime("%d/%m/%Y")

    # Verificar que la función devuelve la fecha actual
    assert obtener_fecha() == fecha_actual
