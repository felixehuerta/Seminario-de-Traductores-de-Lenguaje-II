import tkinter as tk       
from tkinter import ttk
from analisis_lexico import analizar
from analisis_sintactico import Verificar
from analisis_semantico import analizar_semantica

def obtener_tokens_desde_archivo():

    tokens = []

    with open("tokens.txt", "r", encoding="utf-8") as file:

        for linea in file:

            partes = linea.strip().split()

            if len(partes) >= 3:
                tokens.append((partes[0], partes[1], partes[2]))

    return tokens

codigo_fuente = ""          
lexico_analizado = False    
sintaxis_analizado = False  


def mostrar_resultados(mensaje):                #Imprime el recuadro principal, para mostar mensaje de error
    global salida_sintactico
    salida_sintactico.config(state=tk.NORMAL)
    salida_sintactico.delete("1.0", tk.END)
    salida_sintactico.insert(tk.END, mensaje)
    salida_sintactico.config(state=tk.DISABLED)

#Funcion de los botones 
def mostrar_lectura_archivo(widget_texto):      #Funcion para boton de volver a guardar
    global codigo_fuente
    # ARCHIVO DE ENTRADA
    with open("Entrada.txt","r", encoding='utf-8') as file:
        codigo_fuente=file.read()
        widget_texto.config(state=tk.NORMAL)
        widget_texto.delete("1.0", tk.END)
        widget_texto.insert(tk.END, codigo_fuente)

def guardar_archivo(widget_texto):              #Boton para guardar cambios
    global codigo_fuente
    # ARCHIVO DE ENTRADA
    with open("Entrada.txt","w", encoding='utf-8') as file:
        codigo_fuente = widget_texto.get("1.0", tk.END)
        file.write(codigo_fuente)
        mostrar_resultados("Los cambios se han guardado. ")

def mostrar_analisis_lexico():                  #Boton analisar lexico
    global codigo_fuente, lexico_analizado, sintaxis_analizado
    lexico_analizado = False
    sintaxis_analizado = False

    if not (codigo_fuente):
        mostrar_resultados("Debe cargar el codigo fuente primero. ")
        return 
    if texto_entrada.get("1.0", tk.END) != codigo_fuente:
        mostrar_resultados("Hay cambios sin guardar. ")
        return
    # Hacer el analisis y guardar los resultados
    resultados_analisis = analizar(codigo_fuente)
    if "Error" in resultados_analisis:
        mostrar_resultados(resultados_analisis)
        return
    # Limpiar tabla y archivo de salida, despues escribir los nuevos resultados
    with open("tokens.txt", 'w', encoding="utf-8"):              
        for item in tabla_tokens.get_children():
            tabla_tokens.delete(item)
    with open("tokens.txt", "r+", encoding='utf-8') as file:
        for i in resultados_analisis:
            file.writelines(i)
            file.write("\n")
            tabla_tokens.insert('', 'end', values=i.split())
        lexico_analizado = True
        mostrar_resultados("Analisis lexico correcto. ")

def mostrar_analisis_sintactico():

    global lexico_analizado
    global sintaxis_analizado

    sintaxis_analizado = False

    if not lexico_analizado:
        mostrar_resultados("Se necesita análisis léxico primero.")
        return

    resultado_sintactico = Verificar()

    mostrar_resultados(resultado_sintactico)

    if "correcto" in resultado_sintactico.lower():
        sintaxis_analizado = True
        

def mostrar_analisis_semantico():

    global sintaxis_analizado

    if not sintaxis_analizado:
        mostrar_resultados("Se necesita el analisis sintactico primero.")
        return

    tokens = obtener_tokens_desde_archivo()

    resultado = analizar_semantica(tokens)

    mostrar_resultados(resultado)
    
#Interfaz grafica
ventana = tk.Tk()
ventana.title("Analizador lexico y sintactico")
ventana.config(bg="pale turquoise")

# Widget de texto  "Entrada.txt"
texto_entrada = tk.Text(ventana, wrap="word", height=14, width=50)
texto_entrada.grid(row=0, column=1, padx=10, pady=10)
texto_entrada.config(state=tk.DISABLED)
texto_entrada.config(bg="snow")
# Tabla para mostrar los datos del lexico
tabla_tokens = ttk.Treeview(ventana, columns=('Token', 'Lexema', 'Linea'), show='headings')
tabla_tokens.heading('Token', text='Token')
tabla_tokens.heading('Lexema', text='Lexema')
tabla_tokens.heading('Linea', text='Linea')
tabla_tokens.grid(row=0, column=0, padx=10, pady=10)

# Salida de los resultados de los analisis 
salida_sintactico = tk.Text(ventana, wrap="word", height=5, width=100)
salida_sintactico.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
salida_sintactico.config(state=tk.DISABLED)
salida_sintactico.config(bg="sky blue")

mostrar_lectura_archivo(texto_entrada)
# Botón para leer "Entrada.txt"
boton_leer_entrada = tk.Button(ventana, text="Volver a cargar archivo", command=lambda: mostrar_lectura_archivo(texto_entrada))
boton_leer_entrada.grid(row=1, column=0, pady=10, padx=10, sticky=tk.W)
boton_leer_entrada.config(bg="steel blue")
# Botón para guardar archivo "Entrada.txt"
boton_guardar = tk.Button(ventana, text="Guardar cambios", command=lambda: guardar_archivo(texto_entrada))
boton_guardar.grid(row=1, column=0, pady=10, padx=10)
boton_guardar.config(bg="steel blue")
# Botón para leer y mostrar el contenido del archivo de entrada 
boton_analisis_lexico = tk.Button(ventana, text="Analisis Lexico", command=mostrar_analisis_lexico)
boton_analisis_lexico.grid(row=3, column=0,  pady=10, padx=10)
boton_analisis_lexico.config(bg="steel blue")
# Botón para hacer el analisis sintactico del codigo cargado
boton_analisis_sintactico = tk.Button(ventana, text="Analisis Sintactico", command=lambda: mostrar_analisis_sintactico())
boton_analisis_sintactico.grid(row=3, column=0, columnspan=2, pady=10, padx=10)
boton_analisis_sintactico.config(bg="steel blue")
# Botón para hacer el analisis semantico
boton_analisis_semantico = tk.Button(
    ventana,
    text="Analisis Semantico",
    command=mostrar_analisis_semantico
)
boton_analisis_semantico.grid(row=3, column=1, pady=10, padx=10)
boton_analisis_semantico.config(bg="steel blue")
# Ejecutar el bucle principal de la ventana
ventana.mainloop()