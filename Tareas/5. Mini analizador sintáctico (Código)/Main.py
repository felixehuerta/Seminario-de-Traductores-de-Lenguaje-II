"""
Programa Principal (Main)

Este archivo coordina la ejecución del analizador léxico y
del analizador sintáctico, simulando el funcionamiento básico
de un compilador en sus primeras etapas.

Se han añadido pausas entre cada fase del análisis para permitir
al usuario observar los resultados antes de continuar con la
siguiente etapa del proceso.

Además, se ha mejorado la presentación de los resultados para
hacerlos más claros, organizados y fáciles de interpretar,
utilizando separadores visuales y formato tipo tabla.

El flujo del programa es el siguiente:

1. El usuario ingresa una cadena de entrada.
2. El analizador léxico procesa la cadena y genera una lista de tokens.
3. Se muestran los tokens en formato tabular.
4. Se realiza una pausa para revisión del usuario.
5. Los tokens se transforman al formato requerido por el parser.
6. Se muestra la cadena de entrada del parser.
7. El analizador sintáctico evalúa la estructura usando una tabla LR.
8. Se muestra el resultado del análisis sintáctico.
9. Se realiza una pausa final.

                    ESTRUCTURA DEL PROGRAMA
---------------------------------------------------------
| Entrada → Léxico → (PAUSA) → Parser LR → (PAUSA) → Fin |
---------------------------------------------------------

                    MEJORAS IMPLEMENTADAS
---------------------------------------------------------
| Mejora                    | Descripción               |
|---------------------------|---------------------------|
| Salida tabular            | Tokens alineados          |
| Separadores visuales      | Mejor lectura             |
| Pausas                    | Control del flujo         |
| Claridad en parser        | Entrada más entendible    |
---------------------------------------------------------

Autor: [ESTRADA HUERTA FÉLIX EDUARDO - 216819883]
"""

from Analizador_Lexico import analizar_lexico
from Analizador_Sintactico import convertir_tokens, parser_lr

def linea():
    print("-" * 60)

def pausa(mensaje="Presiona ENTER para continuar..."):
    input(f"\n{mensaje}")

def imprimir_tokens(tokens):
    print("\nTOKENS GENERADOS:")
    linea()
    print(f"{'LEXEMA':<15}{'TOKEN':<20}{'TIPO':<10}")
    linea()

    for lexema, token, tipo in tokens:
        print(f"{lexema:<15}{token:<20}{tipo:<10}")

    linea()

def main():
    entrada = input("Cadena a analizar: ")

    # ===============================
    # ANÁLISIS LÉXICO
    # ===============================
    print("\n" + "="*20 + " ANÁLISIS LÉXICO " + "="*20)
    tokens = analizar_lexico(entrada)

    imprimir_tokens(tokens)

    pausa("Fin análisis léxico.\nPresiona ENTER para continuar al análisis sintáctico...")

    # ===============================
    # CONVERSIÓN DE TOKENS
    # ===============================
    print("\n" + "="*18 + " TOKENS PARA PARSER " + "="*18)
    tokens_parser = convertir_tokens(tokens)

    print("\nEntrada del parser:")
    linea()
    print(" ".join(tokens_parser))
    linea()

    pausa("Tokens listos.\nPresiona ENTER para iniciar el análisis sintáctico...")

    # ===============================
    # ANÁLISIS SINTÁCTICO
    # ===============================
    print("\n" + "="*18 + " ANÁLISIS SINTÁCTICO " + "="*18)
    parser_lr(tokens_parser)

    pausa("Fin análisis sintáctico.\nPresiona ENTER para finalizar el programa...")

if __name__ == "__main__":
    main()