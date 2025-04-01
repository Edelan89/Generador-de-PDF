import openpyxl
from excell_utils import cargar_excel, escribir_excel
import os


def test_cargar_excel():
    # Crear un archivo Excel de prueba
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet['A1'] = 'Test Data'
    test_file = 'test_excel.xlsx'
    workbook.save(test_file)

    # Llamar a la función cargar_excel
    loaded_sheet = cargar_excel(test_file)

    # Verificar que la función devuelve un objeto de hoja de cálculo
    assert isinstance(loaded_sheet, openpyxl.worksheet.worksheet.Worksheet)

    # Verificar que los datos se cargaron correctamente
    assert loaded_sheet['A1'].value == 'Test Data'

    # Eliminar el archivo de prueba
    os.remove(test_file)
