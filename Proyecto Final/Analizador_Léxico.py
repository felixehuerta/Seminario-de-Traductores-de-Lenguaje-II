"""
Analizador Léxico Completo

Para el desarrollo de este analizador léxico, se han de definir
el como se analizarán los tokens según la tabla de simbolos
entregada.

                    TABLA DE SIMBOLOS
---------------------------------------------------------
| Token                     | Expresión Regular         |
|---------------------------|---------------------------|
| IDENTIFICADOR             | letra (letra|digito)*     |
| ENTERO                    | digito+                   |
| REAL                      | entero.entero             |
| OPERADOR DE ADICIÓN       | + | -                     |
| OPERADOR DE MULTIPLICACIÓN| * | /                     |
| OPERADOR DE ASIGNACIÓN    | =                         |
| OPERADOR RELACIONAL       | == | != | < | > | <= | >= |
| OPERADOR LÓGICO AND       | &&                        |
| OPERADOR LÓGICO OR        | ||                        |
| OPERADOR LÓGICO NOT       | !                         |
| PARENTESIS                | ( , )                     |
| LLAVES                    | { , }                     |
| PUNTO Y COMA              | ;                         |
---------------------------------------------------------

PALABRAS RESERVADAS: if, else, while, return, int, float

                VALORES DE TIPO
---------------------------------------------
| Simbolo       |  Tipo |                   |
|---------------|-------|-------------------|
| IDENTIFICADOR | 0     |                   |
| ENTERO        | 1     |                   |
| REAL          | 2     |                   |
| CADENA        | 3     |                   |
| TIPO          | 4     | int,float,void    |
| opSUMA        | 5     | +,-               |
| opMUL         | 6     | *,/               |
| opRELAC       | 7     | <,<=,>,>=         |
| opOR          | 8     | ||                |
| opAND         | 9     | &&                |
| opNOT         | 10    | !                 |
| opIGUALDAD    | 11    | ==, !=            |
| ;             | 12    |                   |
| ,             | 13    |                   |
| (             | 14    |                   |
| )             | 15    |                   |
| {             | 16    |                   |
| }             | 17    |                   |
| =             | 18    |                   |
| IF            | 19    |                   |
| WHILE         | 20    |                   |
| RETURN        | 21    |                   |
| ELSE          | 22    |                   |
| $             | 23    |                   |
---------------------------------------------

Autor: [ESTRADA HUERTA FÉLIX EDUARDO - 216819883]
"""
import re

# PALABRAS RESERVADAS
PALABRAS_RESERVADAS = {
    "if": 19,
    "while": 20,
    "return": 21,
    "else": 22,
    "int": 4,
    "float": 4,
    "void": 4
}

# ESPECIFICACIÓN DE TOKENS
TOKENS = [
    ("opIGUALDAD", r"==|!="),
    ("opRELAC", r"<=|>=|<|>"),
    ("opAND", r"&&"),
    ("opOR", r"\|\|"),
    ("REAL", r"\d+\.\d+"),
    ("ENTERO", r"\d+"),
    ("IDENTIFICADOR", r"[a-zA-Z][a-zA-Z0-9]*"),
    ("opSUMA", r"\+|-"),
    ("opMUL", r"\*|/"),
    ("opNOT", r"!"),
    ("=", r"="),
    (";", r";"),
    (",", r","),
    ("(", r"\("),
    (")", r"\)"),
    ("{", r"\{"),
    ("}", r"\}"),
    ("ESPACIO", r"[ \t\n]+"),
    ("ERROR", r".")
]

# MAPA DE TIPOS
TIPOS = {
    "IDENTIFICADOR": 0,
    "ENTERO": 1,
    "REAL": 2,
    "CADENA": 3,
    "TIPO": 4,
    "opSUMA": 5,
    "opMUL": 6,
    "opRELAC": 7,
    "opOR": 8,
    "opAND": 9,
    "opNOT": 10,
    "opIGUALDAD": 11,
    ";": 12,
    ",": 13,
    "(": 14,
    ")": 15,
    "{": 16,
    "}": 17,
    "=": 18,
    "IF": 19,
    "WHILE": 20,
    "RETURN": 21,
    "ELSE": 22,
    "$": 23
}

# FUNCIÓN PRINCIPAL
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

                # Ignorar espacios
                if tipo == "ESPACIO":
                    posicion = match.end()
                    break

                # Palabras reservadas
                if tipo == "IDENTIFICADOR" and lexema in PALABRAS_RESERVADAS:
                    tipo_token = lexema.upper()
                    valor_tipo = PALABRAS_RESERVADAS[lexema]
                else:
                    tipo_token = tipo
                    valor_tipo = TIPOS.get(tipo, -1)

                if tipo_token == "ERROR":
                    print(f"ERROR LÉXICO: símbolo no reconocido '{lexema}'")
                else:
                    print(f"{lexema:<12} -> {tipo_token:<15} Tipo: {valor_tipo}")

                tokens_encontrados.append((lexema, tipo_token, valor_tipo))
                posicion = match.end()
                break

        if not match:
            print(f"ERROR LÉXICO en posición {posicion}")
            break

    tokens_encontrados.append(("$", "$", 23))
    print("$           -> FIN             Tipo: 23")

    return tokens_encontrados

# EJECUCIÓN DEL PROGRAMA
entrada = input("Cadena a analizar: ")
analizar_lexico(entrada)

"""
EJEMPLO DE CADENA DE EJECUCIÓN:

int x = 10;
float y = 3.14;
if (x >= 10 && y != 0.0) {
    x = x + 1;
    y = y * 2.5;
} else {
    return x;
}

"""