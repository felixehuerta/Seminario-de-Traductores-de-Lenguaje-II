"""
Analizador Sintáctico para la gramática dada:
E → E + id | id

Autor: [ESTRADA HUERTA FÉLIX EDUARDO - 216819883]
"""

# Conversión de tokens del léxico a formato del parser
def convertir_tokens(tokens):
    resultado = []

    for lexema, tipo, _ in tokens:
        if tipo == "IDENTIFICADOR":
            resultado.append("id")
        elif lexema == "+":
            resultado.append("+")
        elif lexema == "$":
            resultado.append("$")

    return resultado


# Tabla LR (Ejercicio 2)
tabla_lr = {
    0: {"id": ("d", 2), "E": 1},
    1: {"$": ("r", 0)},
    2: {"+": ("d", 3), "$": ("r", 2)},
    3: {"id": ("d", 2), "E": 4},
    4: {"$": ("r", 1)}
}

# Reglas
reglas = {
    1: ("E", ["id", "+", "E"]),
    2: ("E", ["id"])
}


def parser_lr(tokens):
    pila = [0]
    entrada = tokens.copy()
    paso = 1

    print("\nANÁLISIS SINTÁCTICO\n")

    while True:
        estado = pila[-1]
        simbolo = entrada[0]

        accion = tabla_lr.get(estado, {}).get(simbolo)

        print(f"Paso {paso}")
        print(f"Pila: {pila}")
        print(f"Entrada: {entrada}")

        if accion is None:
            print("❌ ERROR SINTÁCTICO")
            break

        tipo = accion[0]

        if tipo == "d":  # SHIFT
            pila.append(simbolo)
            pila.append(accion[1])
            entrada.pop(0)
            print(f"SHIFT -> {accion[1]}\n")

        elif tipo == "r":  # REDUCE
            regla = accion[1]

            if regla == 0:
                print("✅ CADENA ACEPTADA")
                break

            izq, der = reglas[regla]

            print(f"REDUCE {izq} → {' '.join(der)}")

            for _ in range(len(der) * 2):
                pila.pop()

            estado = pila[-1]
            pila.append(izq)
            pila.append(tabla_lr[estado][izq])

            print(f"Pila: {pila}\n")

        paso += 1