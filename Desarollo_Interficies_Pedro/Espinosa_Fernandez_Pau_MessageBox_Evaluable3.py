import tkinter as tk
from tkinter import messagebox

def mostrar_pregunta():
    var_fe = messagebox.askquestion('Pregunta', 'Vols continuar?')
    etiqueta.config(text="Has clicat: " + var_fe)

def mostrar_pregunta_cancelar():
    var_fe = messagebox.askokcancel('Pregunta', 'Vols continuar?')
    etiqueta.config(text="Has clicat: " + str(var_fe))

def mostrar_pregunta_si_no():
    var_fe = messagebox.askyesno('Pregunta', 'Vols continuar?')
    etiqueta.config(text="Has clicat: " + str(var_fe))

ventana = tk.Tk()
ventana.title("Finestres Emergents")

boto_pregunta = tk.Button(ventana, text="Pregunta", command=mostrar_pregunta)
boto_pregunta.pack(pady=10)

boto_pregunta_cancelar = tk.Button(ventana, text="Pregunta amb Cancel·lar", command=mostrar_pregunta_cancelar)
boto_pregunta_cancelar.pack(pady=10)

boto_si_no = tk.Button(ventana, text="Pregunta Sí/No", command=mostrar_pregunta_si_no)
boto_si_no.pack(pady=10)

etiqueta = tk.Label(ventana, text="")
etiqueta.pack(pady=10)

ventana.mainloop()




