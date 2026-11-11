import tkinter as tk
from dotenv import load_dotenv
import os


load_dotenv()

APP_USER = os.getenv("APP_USER")
APP_PASSWORD = os.getenv("APP_PASSWORD")


def capturar_credenciales():
    usuario = entrada_usuario.get()
    contrasena = entrada_password.get()

    validar_credenciales(usuario, contrasena)



def validar_credenciales(usuario, contrasena):
    if usuario == APP_USER and contrasena == APP_PASSWORD:
        mostrar_mensaje("Acceso correcto", "green")
    else:
        mostrar_mensaje(
            "Usuario o contraseña incorrectos", "red"
        )



def mostrar_mensaje(mensaje, color):
    etiqueta_mensaje.config(text=mensaje, fg=color)



ventana = tk.Tk()
ventana.title("Validación de credenciales")
ventana.geometry("400x300")
ventana.resizable(False, False)


titulo = tk.Label(
    ventana,
    text="Inicio de sesión",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=20)


tk.Label(ventana, text="Usuario:").pack()

entrada_usuario = tk.Entry(ventana, width=30)
entrada_usuario.pack(pady=5)


tk.Label(ventana, text="Contraseña:").pack()

entrada_password = tk.Entry(
    ventana, width=30, show="*"
)
entrada_password.pack(pady=5)


boton = tk.Button(
    ventana,
    text="Iniciar sesión",
    command=capturar_credenciales
)
boton.pack(pady=15)


etiqueta_mensaje = tk.Label(
    ventana,
    text="",
    font=("Arial", 11, "bold")
)
etiqueta_mensaje.pack(pady=10)


ventana.mainloop()