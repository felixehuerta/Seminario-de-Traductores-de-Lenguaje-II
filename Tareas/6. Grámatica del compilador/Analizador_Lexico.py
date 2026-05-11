"""
Analizador Léxico

Este módulo reconoce tokens de entrada usando expresiones regulares.

✔ Identifica identificadores, operadores y símbolos
✔ Retorna tokens en formato (lexema, tipo, valor)
✔ Compatible con el parser LR del PDF

Autor: [ESTRADA HUERTA FÉLIX EDUARDO - 216819883]
"""

import re

TOKENS = [
    ("IDENTIFICADOR", r"[a-zA-Z][a-zA-Z0-9]*"),
    ("opSUMA", r"\+"),
    ("opMUL", r"\*"),
    ("ESPACIO", r"[ \t\n]+"),
    ("ERROR", r".")
]

TIPOS = {
    "IDENTIFICADOR": 0,
    "opSUMA": 5,
    "opMUL": 6,
    "$": 23
}


def analizar_lexico(cadena):
    posicion = 0
    tokens_encontrados = []

    while posicion < len(cadena):
        match = None

        for tipo, patron in TOKENS:
            regex = re.compile(patron)
            match = regex.match(cadena, posicion)

            if match:
                lexema = match.group(0)

                if tipo == "ESPACIO":
                    posicion = match.end()
                    break

                if tipo == "ERROR":
                    print(f"ERROR LÉXICO: {lexema}")
                    return []

                valor = TIPOS.get(tipo, -1)

                tokens_encontrados.append((lexema, tipo, valor))
                posicion = match.end()
                break

    tokens_encontrados.append(("$", "$", 23))
    return tokens_encontrados