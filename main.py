import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import ctypes  # Para ocultar el ícono de la pluma en la barra de tareas


# Función para generar la contraseña
def generar_contrasena():
    longitud = int(slider_longitud.get())

    opciones = ""
    if var_mayusculas.get():
        opciones += string.ascii_uppercase
    if var_minusculas.get():
        opciones += string.ascii_lowercase
    if var_numeros.get():
        opciones += string.digits
    if var_caracteres.get():
        opciones += string.punctuation

    if not opciones:
        messagebox.showerror("Error", "Seleccione al menos una opción para generar la contraseña.")
        return

    contrasena = ''.join(random.choice(opciones) for _ in range(longitud))

    entrada_contrasena.config(state="normal")
    entrada_contrasena.delete(0, tk.END)
    entrada_contrasena.insert(0, contrasena)
    entrada_contrasena.config(state="readonly")


# Función para copiar la contraseña al portapapeles
def copiar_portapapeles():
    contrasena = entrada_contrasena.get()
    if contrasena:
        ventana.clipboard_clear()
        ventana.clipboard_append(contrasena)
        ventana.update()
        #messagebox.showinfo("Copiado", "La contraseña ha sido copiada al portapapeles.")


# Función para actualizar la etiqueta dinámica del slider
def actualizar_etiqueta_longitud(valor):
    etiqueta_valor_longitud.config(text=f"{int(float(valor))} caracteres")


# Establecer el ícono invisible en la barra de tareas
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("password_generator")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("500x500")
ventana.resizable(False, False)

# Cambiar fuente general
ventana.option_add("*Font", " 12")

# Etiqueta de título
etiqueta_titulo = tk.Label(ventana, text="Generador de Contraseñas", font=("Roboto", 18))
etiqueta_titulo.pack(pady=10)

# Frame para las opciones de complejidad
frame_opciones = tk.LabelFrame(ventana, text="Opciones de Complejidad", padx=10, pady=10)
frame_opciones.pack(pady=10, padx=10, fill="both")

# Variables para las casillas de selección
var_mayusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_caracteres = tk.BooleanVar(value=True)

# Casillas de selección en columnas
check_mayusculas = ttk.Checkbutton(frame_opciones, text="Letras Mayúsculas", variable=var_mayusculas)
check_mayusculas.grid(row=0, column=0, sticky="w", padx=10, pady=5)
check_minusculas = ttk.Checkbutton(frame_opciones, text="Letras Minúsculas", variable=var_minusculas)
check_minusculas.grid(row=1, column=0, sticky="w", padx=10, pady=5)
check_numeros = ttk.Checkbutton(frame_opciones, text="Números", variable=var_numeros)
check_numeros.grid(row=0, column=1, sticky="w", padx=10, pady=5)
check_caracteres = ttk.Checkbutton(frame_opciones, text="Caracteres Especiales", variable=var_caracteres)
check_caracteres.grid(row=1, column=1, sticky="w", padx=10, pady=5)

# Slider para la longitud de la contraseña
frame_longitud = tk.Frame(ventana)
frame_longitud.pack(pady=10)

etiqueta_longitud = tk.Label(frame_longitud, text="Longitud de la contraseña:")
etiqueta_longitud.pack()
slider_longitud = ttk.Scale(
    frame_longitud, from_=8, to=32, orient="horizontal", length=300, command=actualizar_etiqueta_longitud
)
slider_longitud.set(12)
slider_longitud.pack()

etiqueta_valor_longitud = tk.Label(frame_longitud, text="12 caracteres", font=("Roboto", 10))
etiqueta_valor_longitud.pack(pady=5)

# Entrada para mostrar la contraseña generada
frame_salida = tk.Frame(ventana)
frame_salida.pack(pady=10)

entrada_contrasena = ttk.Entry(frame_salida, font=("Roboto", 14), justify="center", state="readonly", width=30)
entrada_contrasena.pack()

# Frame para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)

boton_generar = ttk.Button(frame_botones, text="Generar Contraseña", command=generar_contrasena)
boton_generar.grid(row=0, column=0, padx=10)

boton_copiar = ttk.Button(frame_botones, text="Copiar al Portapapeles", command=copiar_portapapeles)
boton_copiar.grid(row=0, column=1, padx=10)

# Ejecutar ventana
ventana.mainloop()
