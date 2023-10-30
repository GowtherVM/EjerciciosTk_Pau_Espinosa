import tkinter as tk


def calcular():
    try:
        resultado.set(eval(entrada.get()))
    except:
        resultado.set("Error")


ventana = tk.Tk()
ventana.title("Calculadora")


resultado = tk.StringVar()


entrada = tk.Entry(ventana, textvariable=resultado, font=("Arial", 20))
entrada.grid(row=0, column=0, columnspan=4)


numeros = "789456123"
fila = 1
columna = 0
for num in numeros:
    tk.Button(ventana, text=num, font=("Arial", 20), command=lambda num=num: entrada.insert(tk.END, num)).grid(row=fila, column=columna)
    columna += 1
    if columna > 2:
        columna = 0
        fila += 1


botones = {
    "0": (1, 1),
    ".": (1, 2),
    "+": (1, 3),
    "-": (2, 3),
    "*": (3, 3),
    "/": (4, 3),
    "C": (4, 0),
    "=": (4, 1)
}

for texto, posicion in botones.items():
    tk.Button(ventana, text=texto, font=("Arial", 20), command=lambda texto=texto: entrada.insert(tk.END, texto) if texto != "C" else entrada.delete(0, tk.END)).grid(row=posicion[0], column=posicion[1])


tk.Button(ventana, text="=", font=("Arial", 20), command=calcular).grid(row=4, column=2, columnspan=2)


ventana.mainloop()