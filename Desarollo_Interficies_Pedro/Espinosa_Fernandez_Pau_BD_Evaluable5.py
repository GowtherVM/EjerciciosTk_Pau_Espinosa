import tkinter as tk
import sqlite3

#Me he ayudado con chatGPT no me quedaba muy claro

def insertar_datos():
    conexion = sqlite3.connect("base_de_datos.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO tabla_de_la_BD VALUES (?, ?, ?)", (entry_nombre.get(), entry_apellido.get(), entry_edad.get()))
    conexion.commit()
    conexion.close()
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)


def imprimir_resultados():
    conexion = sqlite3.connect("base_de_datos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tabla_de_la_BD")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)
    conexion.close()


root = tk.Tk()
root.title("Interfaz para Base de Datos")


tk.Label(root, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Apellido:").grid(row=1, column=0)
entry_apellido = tk.Entry(root)
entry_apellido.grid(row=1, column=1)

tk.Label(root, text="Edad:").grid(row=2, column=0)
entry_edad = tk.Entry(root)
entry_edad.grid(row=2, column=1)

tk.Button(root, text="Introducir Datos", command=insertar_datos).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Imprimir Resultados", command=imprimir_resultados).grid(row=4, column=0, columnspan=2)

root.mainloop()