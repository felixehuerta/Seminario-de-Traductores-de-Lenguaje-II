"""
Programa Principal (Main)

Este archivo coordina la ejecución del analizador léxico y
del analizador sintáctico, simulando el funcionamiento básico
de un compilador en sus primeras etapas.

FLUJO:
1. Entrada del usuario
2. Análisis léxico
3. Conversión a formato del parser (IDs numéricos)
4. Análisis sintáctico usando tabla LR (.lr)

IMPORTANTE:
El parser trabaja con índices numéricos (columnas de la tabla LR),
tal como lo especifica el archivo .inf del PDF.

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
    # CONVERSIÓN A IDs (PDF)
    # ===============================
    print("\n" + "="*18 + " TOKENS PARA PARSER " + "="*18)
    tokens_parser = convertir_tokens(tokens)

    print("\nEntrada del parser (IDs):")
    linea()
    print(tokens_parser)
    linea()

    pausa("Tokens listos.\nPresiona ENTER para iniciar el análisis sintáctico...")

    # ===============================
    # ANÁLISIS SINTÁCTICO
    # ===============================
    print("\n" + "="*18 + " ANÁLISIS SINTÁCTICO " + "="*18)
    parser_lr(tokens_parser, "gramatica5.lr")

    pausa("Fin análisis sintáctico.\nPresiona ENTER para finalizar el programa...")


if __name__ == "__main__":
    main()