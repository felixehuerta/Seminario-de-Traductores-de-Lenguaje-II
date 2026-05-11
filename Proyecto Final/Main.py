import tkinter as tk
from tkinter import ttk
from analisis_lexico import analizar
from analisis_sintactico import Verificar
from analisis_semantico import analizar_semantica

codigo_fuente = ""
lexico_analizado = False

def obtener_tokens():
    tokens = []
    with open("tokens.txt", "r") as f:
        for linea in f:
            tokens.append(linea.strip().split())
    return tokens

def mostrar_resultados(msg):
    salida.config(state=tk.NORMAL)
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, msg)
    salida.config(state=tk.DISABLED)

def lexico():
    global lexico_analizado
    res = analizar(codigo_fuente)

    if isinstance(res, str):
        mostrar_resultados(res)
        return

    with open("tokens.txt", "w") as f:
        for r in res:
            f.write(r + "\n")

    lexico_analizado = True
    mostrar_resultados("Lexico correcto")

def sintactico():
    if not lexico_analizado:
        mostrar_resultados("Primero léxico")
        return

    res = Verificar()
    mostrar_resultados(res)

    tokens = obtener_tokens()
    sem = analizar_semantica(tokens)

    ventana = tk.Toplevel()
    tk.Label(ventana, text=sem).pack()

ventana = tk.Tk()

salida = tk.Text(ventana)
salida.pack()

tk.Button(ventana, text="Lexico", command=lexico).pack()
tk.Button(ventana, text="Sintactico", command=sintactico).pack()

with open("Entrada.txt") as f:
    codigo_fuente = f.read()

ventana.mainloop()