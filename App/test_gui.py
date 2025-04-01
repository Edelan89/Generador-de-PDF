import pytest
import tkinter as tk
from gui import crear_interfaz


def test_crear_interfaz():
    root = tk.Tk()
    entries = crear_interfaz(root)

    # Verificar que se crean los widgets Entry
    for entry in entries:
        assert isinstance(entry, tk.Entry)
