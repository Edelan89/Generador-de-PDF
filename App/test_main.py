import pytest
import tkinter as tk
from main import main
from unittest.mock import patch


def test_main():
    with patch("main.tk.Tk") as mock_tk:
        # Crear una instancia simulada de Tk
        mock_root = mock_tk.return_value

        # Simular la ejecución de main()
        main()

        # Verificar que se llamó a Tk()
        assert mock_tk.call_count == 1

        # Verificar que se llamó a title() con el título correcto
        mock_root.title.assert_called_once_with("Formulario de Pacientes")

        # Verificar que se llamó a mainloop()
        mock_root.mainloop.assert_called_once()
