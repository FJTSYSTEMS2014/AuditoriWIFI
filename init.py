import tkinter as tk
from tkinter import PhotoImage
import subprocess
import os
import importlib

def verificar_bibliotecas():
    bibliotecas_faltantes = []
    
    # Lista de bibliotecas a verificar
    bibliotecas = ["tkinter", "PIL", "subprocess"]
    
    for lib in bibliotecas:
        try:
            importlib.import_module(lib)
        except ImportError:
            bibliotecas_faltantes.append(lib)
    
    return bibliotecas_faltantes

def instalar_bibliotecas():
    bibliotecas_faltantes = verificar_bibliotecas()
    
    if not bibliotecas_faltantes:
        return
    
    mensaje = "Las siguientes bibliotecas son necesarias pero no están instaladas:\n\n"
    mensaje += "\n".join(bibliotecas_faltantes)
    mensaje += "\n\n¿Deseas instalarlas ahora?"
    
    respuesta = tk.messagebox.askquestion("Instalar Bibliotecas", mensaje)
    
    if respuesta == "yes":
        for lib in bibliotecas_faltantes:
            subprocess.Popen(["pip", "install", lib])
            tk.messagebox.showinfo("Instalación Completada", f"{lib} ha sido instalada.")

def ejecutar_scripts1():
    comando1 = "xfce4-terminal -e 'python AuditoriWIFI.py'"
    subprocess.Popen(comando1, shell=True)

def ejecutar_scripts2():
    comando2 = "xfce4-terminal -e 'python DesAuntenticar.py'"
    subprocess.Popen(comando2, shell=True)
def ejecutar_scripts3():
    comando3 = "xfce4-terminal -e 'python AtaqueDiccionario.py'"
    subprocess.Popen(comando3, shell=True)
    
def abrir_carpeta():
    carpeta_trafico = "trafico"
    if os.path.exists(carpeta_trafico) and os.path.isdir(carpeta_trafico):
        os.system("xdg-open " + carpeta_trafico)
def abrir_carpeta2():
    carpeta_diccionario = "diccionario"
    if os.path.exists(carpeta_diccionario ) and os.path.isdir(carpeta_diccionario):
        os.system("xdg-open " + carpeta_diccionario)

def salir():
    root.destroy()

# Verificar e instalar bibliotecas faltantes
instalar_bibliotecas()

root = tk.Tk()
root.title("Auditoria-WIFI-@FranckTscherig")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Cargar la imagen GIF
imagen = PhotoImage(file="img/r.gif")
imagen_label = tk.Label(frame, image=imagen)
imagen_label.pack()
# Agregar la leyenda
leyenda_label = tk.Label(frame, text="Autor: @FranckTscherig")
leyenda_label.pack()

boton_ejecutar1 = tk.Button(frame, text="Ejecutar AuditoriWIFI.py", command=ejecutar_scripts1)
boton_ejecutar2 = tk.Button(frame, text="Ejecutar DesAuntenticar.py", command=ejecutar_scripts2)
boton_ejecutar3 = tk.Button(frame, text="Ejecutar AtaqueDiccionario.py", command=ejecutar_scripts3)
boton_abrir_carpeta = tk.Button(frame, text="Abrir Carpeta 'trafico'", command=abrir_carpeta)
boton_abrir_carpeta2 = tk.Button(frame, text="Abrir Carpeta 'diccionario'", command=abrir_carpeta2)
boton_salir = tk.Button(frame, text="Salir", command=salir)

boton_ejecutar1.pack()
boton_ejecutar2.pack()
boton_abrir_carpeta.pack()
boton_abrir_carpeta2.pack()
boton_ejecutar3.pack()
boton_salir.pack()

root.mainloop()
