import tkinter as tk
from tkinter import ttk, messagebox
import random
import string


# Función para generar la contraseña
def generar_contrasena():
    # Obtener la longitud desde el slider y convertir a entero
    longitud = int(slider_longitud.get())

    # Construir las opciones en base a los checkboxes seleccionados
    opciones = ""
    if var_mayusculas.get():
        opciones += string.ascii_uppercase
    if var_minusculas.get():
        opciones += string.ascii_lowercase
    if var_numeros.get():
        opciones += string.digits
    if var_caracteres.get():
        opciones += string.punctuation

    # Verificar que se haya seleccionado al menos una opción
    if not opciones:
        messagebox.showerror("Error", "Seleccione al menos una opción para generar la contraseña.")
        return

    # Generar contraseña aleatoria
    contrasena = ''.join(random.choice(opciones) for _ in range(longitud))

    # Mostrar la contraseña en el campo de entrada
    entrada_contrasena.config(state="normal")  # Hacer editable temporalmente
    entrada_contrasena.delete(0, tk.END)  # Limpiar contenido previo
    entrada_contrasena.insert(0, contrasena)  # Insertar nueva contraseña
    entrada_contrasena.config(state="readonly")  # Volver a hacerlo solo lectura


# Función para copiar la contraseña al portapapeles
def copiar_portapapeles():
    contrasena = entrada_contrasena.get()
    if contrasena:  # Verificar que haya una contraseña generada
        ventana.clipboard_clear()
        ventana.clipboard_append(contrasena)
        ventana.update()  # Asegurar que el portapapeles se actualice

# Función para actualizar la etiqueta dinámica del slider
def actualizar_etiqueta_longitud(valor):
    etiqueta_valor_longitud.config(text=f"Longitud: {int(float(valor))} caracteres")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("500x450")  # Tamaño inicial de la ventana
ventana.resizable(False, False)

# Etiqueta de título
etiqueta_titulo = tk.Label(ventana, text="Generador de Contraseñas", font=("Arial", 18))
etiqueta_titulo.pack(pady=10)

# Frame para las opciones de complejidad
frame_opciones = tk.LabelFrame(ventana, text="Opciones de Complejidad", padx=10, pady=10)
frame_opciones.pack(pady=10)

# Variables para las casillas de selección
var_mayusculas = tk.BooleanVar(value=True)  # Activadas por defecto
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_caracteres = tk.BooleanVar(value=True)

# Casillas de selección
check_mayusculas = tk.Checkbutton(frame_opciones, text="Letras Mayúsculas", variable=var_mayusculas)
check_mayusculas.grid(row=0, column=0, sticky="w", padx=10, pady=5)
check_minusculas = tk.Checkbutton(frame_opciones, text="Letras Minúsculas", variable=var_minusculas)
check_minusculas.grid(row=1, column=0, sticky="w", padx=10, pady=5)
check_numeros = tk.Checkbutton(frame_opciones, text="Números", variable=var_numeros)
check_numeros.grid(row=0, column=1, sticky="w", padx=10, pady=5)
check_caracteres = tk.Checkbutton(frame_opciones, text="Caracteres Especiales", variable=var_caracteres)
check_caracteres.grid(row=1, column=1, sticky="w", padx=10, pady=5)

# Slider para la longitud de la contraseña
etiqueta_longitud = tk.Label(ventana, text="Longitud de la contraseña:", font=("Arial", 12))
etiqueta_longitud.pack(pady=5)
slider_longitud = ttk.Scale(
    ventana, from_=8, to=32, orient="horizontal", length=300, command=actualizar_etiqueta_longitud
)
slider_longitud.set(12)  # Longitud por defecto
slider_longitud.pack(pady=5)

# Etiqueta dinámica para mostrar el valor del slider
etiqueta_valor_longitud = tk.Label(ventana, text="Longitud: 12 caracteres", font=("Arial", 10))
etiqueta_valor_longitud.pack(pady=5)

# Entrada para mostrar la contraseña generada
entrada_contrasena = ttk.Entry(ventana, font=("Arial", 14), justify="center", state="readonly", width=30)
entrada_contrasena.pack(pady=10)

# Botón para generar contraseña
boton_generar = ttk.Button(ventana, text="Generar Contraseña", command=generar_contrasena)
boton_generar.pack(pady=10)

# Botón para copiar al portapapeles
boton_copiar = ttk.Button(ventana, text="Copiar al Portapapeles", command=copiar_portapapeles)
boton_copiar.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
