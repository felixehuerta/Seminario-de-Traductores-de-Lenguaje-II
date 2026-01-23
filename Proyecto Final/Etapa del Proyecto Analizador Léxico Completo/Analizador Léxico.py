"""
Analizador Léxico Completo
"""
import re

# Definición de Reglas
TOKEN_ID = r'^[a-zA-Z][a-zA-Z0-9]*$'
TOKEN_REAL = r'^[0-9]+\.[0-9]+$'

def analizar_lexico(entrada):
    tokens = entrada.split()
    
    for palabra in tokens:
        if re.match(TOKEN_REAL, palabra):
            print(f"{palabra} -> REAL")
        elif re.match(TOKEN_ID, palabra):
            print(f"{palabra} -> IDENTIFICADOR")
        else:
            print(f"{palabra} -> ERROR LÉXICO")

# Ejecución del Programa
entrada = input("Cadena a analizar: ")
analizar_lexico(entrada)
