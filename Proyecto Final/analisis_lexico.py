import re   

tokens = [
    ('Libreria', r'#include\s+["<].*?[">]'),

    # Palabras reservadas
    ('Reservada_if', r'\bif\b'),
    ('Reservada_void', r'\bvoid\b'),
    ('Reservada_while', r'\bwhile\b'),
    ('Reservada_return', r'\breturn\b'),
    ('Reservada_else', r'\belse\b'),

    # Tipos de datos
    ('Tipo_dato', r'\b(int|char|float|double|long|short|void)\b'),

    # Identificadores
    ('Identificador', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),

    # Cadenas
    ('Cadena', r'"[^"]*"'),

    # 🔥 ORDEN CORREGIDO
    ('Entero', r'\b-?\d+\b'),
    ('Real', r'\b-?\d+\.\d+\b'),

    # Operadores
    ('Op_adicion', r'[+\-]'),
    ('Op_multiplicacion', r'[*/]'),
    ('Op_asignacion', r'='),
    ('Op_relacional', r'(<=|>=|==|!=|<|>)'),

    # Booleanos
    ('Op_binario', r'\b(and|&&|or|\|\|)\b'),

    # Delimitadores
    ('Parentesis_apertura', r'\('),
    ('Parentesis_cierre', r'\)'),
    ('Llave_apertura', r'\{'),
    ('Llave_cierre', r'\}'),
    ('Punto_y_coma', r';'),
    ('Coma', r','),

    ('Espacio', r'\s+')
]

def analizar(codigo):
    resultados = []
    linea = 1

    while codigo:
        encontrado = False

        for token_nombre, patron in tokens:
            coincidencia = re.match(patron, codigo)

            if coincidencia:
                valor = coincidencia.group(0)
                linea += valor.count("\n")

                if token_nombre != "Espacio":
                    valor = valor.replace(" ", "_")
                    resultados.append(f"{token_nombre} {valor} {linea}")

                codigo = codigo[len(valor):]
                encontrado = True
                break

        if not encontrado:
            token_error = ""
            for c in codigo:
                token_error += c
                if c in [" ", "\n"]:
                    break
            return "Error: Token no válido -> " + token_error

    return resultados