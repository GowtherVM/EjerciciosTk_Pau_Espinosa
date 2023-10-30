import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image



ventana = tk.Tk()
ventana.title("Imágenes")

listimg = ["img1.jpg", "img2.jpg", "img3.jpg"]
posicion = 0

def cerrar_pestaña():
    ventana.destroy()

def pasar(direc):
    global posicion
    if direc == "ant" and posicion > 0:
        posicion -= 1
    elif direc == "sig" and posicion < len(listimg) - 1:
        posicion += 1
    actualizar_imagen()
    actualizar_botones()
    actualizar_etiqueta()

def actualizar_imagen():
    img = Image.open('Lista_De_Imagenes/' + listimg[posicion])
    imagen = ImageTk.PhotoImage(img)
    ventana_principal.config(image=imagen)
    ventana_principal.image = imagen

def actualizar_botones():
    if posicion == 0:
        boton_anterior.config(state=tk.DISABLED)
    else:
        boton_anterior.config(state=tk.NORMAL)

    if posicion == len(listimg) - 1:
        boton_siguiente.config(state=tk.DISABLED)
    else:
        boton_siguiente.config(state=tk.NORMAL)

def actualizar_etiqueta():
    num_etiqueta.config(text='Imatge {} de {}'.format(posicion + 1, len(listimg)))

marco_botones = tk.Frame(ventana)
marco_botones.pack(side=tk.BOTTOM, padx=10, pady=10)

ventana.iconbitmap('icon.ico')

imagen = ImageTk.PhotoImage(Image.open('Lista_De_Imagenes/' + listimg[posicion]))
ventana_principal = tk.Label(ventana, image=imagen, padx=10)
ventana_principal.pack()

num_etiqueta = tk.Label(ventana, text='Imatge {} de {}'.format(posicion + 1, len(listimg)), bd=2, relief=tk.SUNKEN, anchor="e")
num_etiqueta.pack(side=tk.BOTTOM, fill=tk.X)

salir = tk.Button(marco_botones, text="Cerrar", command=cerrar_pestaña, pady=10)
salir.pack(side=tk.LEFT, padx=10)
boton_anterior = tk.Button(marco_botones, text="Anterior", command=lambda: pasar("ant"), pady=10)
boton_anterior.pack(side=tk.LEFT, padx=10)
boton_siguiente = tk.Button(marco_botones, text="Siguiente", command=lambda: pasar("sig"), pady=10)
boton_siguiente.pack(side=tk.LEFT, padx=10)




ventana.mainloop()
