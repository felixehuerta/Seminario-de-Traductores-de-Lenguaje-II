"""
Programa Principal (Main)

Este archivo coordina la ejecución del analizador léxico y
del analizador sintáctico, simulando el funcionamiento básico
de un compilador en sus primeras etapas.

Se han añadido pausas entre cada fase del análisis para permitir
al usuario observar los resultados antes de continuar con la
siguiente etapa del proceso.

El flujo del programa es el siguiente:

1. El usuario ingresa una cadena de entrada.
2. El analizador léxico procesa la cadena y genera una lista de tokens.
3. Se muestra el resultado del análisis léxico.
4. Se realiza una pausa para revisión del usuario.
5. Los tokens se transforman al formato requerido por el parser.
6. El analizador sintáctico evalúa la estructura usando una tabla LR.
7. Se muestra el resultado del análisis sintáctico.
8. Se realiza una pausa final.

                    ESTRUCTURA DEL PROGRAMA
---------------------------------------------------------
| Entrada → Léxico → (PAUSA) → Parser LR → (PAUSA) → Fin |
---------------------------------------------------------

Este programa permite validar expresiones como:

Ejemplo 1:
    hola + mundo

Ejemplo 2:
    a + b + c + d + e + f

                    RESULTADOS POSIBLES
---------------------------------------------------------
| Resultado        | Descripción                      |
|------------------|----------------------------------|
| CADENA ACEPTADA  | La sintaxis es correcta          |
| ERROR SINTÁCTICO | La cadena no cumple la gramática |
---------------------------------------------------------

Autor: [ESTRADA HUERTA FÉLIX EDUARDO - 216819883]
"""

from Analizador_Lexico import analizar_lexico
from Analizador_Sintactico import convertir_tokens, parser_lr

def pausa(mensaje="Presiona ENTER para continuar..."):
    input(f"\n{mensaje}")

def main():
    entrada = input("Cadena a analizar: ")

    # ===============================
    # ANÁLISIS LÉXICO
    # ===============================
    print("\n--- ANÁLISIS LÉXICO ---")
    tokens = analizar_lexico(entrada)

    pausa("Fin análisis léxico.\nPresiona ENTER para continuar al análisis sintáctico...")

    # ===============================
    # CONVERSIÓN DE TOKENS
    # ===============================
    print("\n--- TOKENS PARA PARSER ---")
    tokens_parser = convertir_tokens(tokens)
    print(tokens_parser)

    pausa("Tokens listos. \nPresiona ENTER para iniciar el análisis sintáctico...")

    # ===============================
    # ANÁLISIS SINTÁCTICO
    # ===============================
    print("\n--- ANÁLISIS SINTÁCTICO ---")
    parser_lr(tokens_parser)

    pausa("Fin análisis sintáctico.\nPresiona ENTER para finalizar el programa...")

if __name__ == "__main__":
    main()