# src/interfaz.py

import tkinter as tk
from tkinter import messagebox
from main import main  # Importar la función main para ejecutar la detección de plagio

def run_detection():
    # Lógica para ejecutar la detección de plagio
    try:
        main()  # Llama a la función main para ejecutar la detección
        messagebox.showinfo("Info", "Detección de plagio ejecutada.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Detector de Plagio")

# Crear un botón para ejecutar la detección
btn_run = tk.Button(root, text="Ejecutar Detección de Plagio", command=run_detection)
btn_run.pack(pady=20)

# Iniciar el bucle principal de la interfaz
root.mainloop()