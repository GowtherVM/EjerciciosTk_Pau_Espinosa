import os
from tkinter import filedialog as quelcom
from tkinter import *
from PIL import Image, ImageTk

directorio_actual = os.getcwd()

def abrir_imagen():

    tipos_archivos = (("Imágenes", "*.jpg;*.png;*.gif;*.bmp"), ("Todos los archivos", "*.*"))
    ruta_imagen = quelcom.askopenfilename(initialdir=directorio_actual, title="Selecciona una imagen", filetypes=tipos_archivos)

    if ruta_imagen:

        imagen_original = Image.open(ruta_imagen)

        imagen_tk = ImageTk.PhotoImage(imagen_original)
        etiqueta_imagen.config(image=imagen_tk)
        etiqueta_imagen.image = imagen_tk  

        def salvar_imagen():
            ruta_destino = quelcom.asksaveasfile(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if ruta_destino:
                
                imagen_original.save(ruta_destino.name)

        boton_salvar.config(command=salvar_imagen)

ventana = Tk()
ventana.title("Seleccionar y Mostrar Imagen")

boton_abrir_imagen = Button(ventana, text="Abrir Imagen", command=abrir_imagen)
boton_abrir_imagen.pack(pady=20)

etiqueta_imagen = Label(ventana)
etiqueta_imagen.pack()

boton_salvar = Button(ventana, text="Salvar Imagen", state=DISABLED)
boton_salvar.pack(pady=20)

def cerrar_ventana():
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

ventana.mainloop()
