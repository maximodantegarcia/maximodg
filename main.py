from tkinter import *
from ventana import *

def main():
    ventana = Tk()
    ventana.wm_title("Base de datos Sindicato")
    ventana.config(bg='black')
    ventana.geometry('1920x1080')
    app = Registro(ventana)
    app.mainloop()
