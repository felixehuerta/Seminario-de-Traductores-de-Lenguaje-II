"""
Programa Principal (Main)

Este archivo coordina la ejecución del analizador léxico y
del analizador sintáctico, simulando el funcionamiento básico
de un compilador en sus primeras etapas.

El flujo del programa es el siguiente:

1. El usuario ingresa una cadena de entrada.
2. El analizador léxico procesa la cadena y genera una lista de tokens.
3. Los tokens son transformados a un formato simplificado para el parser.
4. El analizador sintáctico evalúa la estructura de la cadena usando
   una tabla LR y una pila.
5. Se muestra si la cadena es aceptada o si existe un error sintáctico.

                    ESTRUCTURA DEL PROGRAMA
---------------------------------------------------------
| Entrada → Análisis Léxico → Tokens → Parser LR → Resultado |
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

Este archivo funciona como punto de entrada del sistema
y conecta todos los módulos desarrollados.

Autor: [ESTRADA HUERTA FÉLIX EDUARDO - 216819883]
"""

from Analizador_Léxico import analizar_lexico
from Analizador_Sintactico import convertir_tokens, parser_lr

def main():
    entrada = input("Cadena a analizar: ")

    print("\n--- ANÁLISIS LÉXICO ---")
    tokens = analizar_lexico(entrada)

    print("\n--- TOKENS PARA PARSER ---")
    tokens_parser = convertir_tokens(tokens)
    print(tokens_parser)

    print("\n--- ANÁLISIS SINTÁCTICO ---")
    parser_lr(tokens_parser)


if __name__ == "__main__":
    main()