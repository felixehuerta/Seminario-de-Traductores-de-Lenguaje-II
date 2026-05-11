"""
Analizador Sintáctico LR(1)

Este módulo implementa un parser LR que valida la estructura
sintáctica utilizando una tabla LR leída desde un archivo .lr.

✔ Usa índices numéricos (columnas)
✔ Sigue exactamente lo indicado en el PDF
✔ Aplica SHIFT / REDUCE

Autor: [ESTRADA HUERTA FÉLIX EDUARDO - 216819883]
"""


def cargar_lr(ruta):
    with open(ruta, "r") as f:
        contenido = f.read().split()

    i = 0

    num_reglas = int(contenido[i])
    i += 1

    id_regla = []
    lon_regla = []
    nombre_regla = []

    for _ in range(num_reglas):
        id_regla.append(int(contenido[i]))
        lon_regla.append(int(contenido[i + 1]))
        nombre_regla.append(contenido[i + 2])
        i += 3

    filas = int(contenido[i])
    columnas = int(contenido[i + 1])
    i += 2

    tabla = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila.append(int(contenido[i]))
            i += 1
        tabla.append(fila)

    return id_regla, lon_regla, nombre_regla, tabla


def convertir_tokens(tokens):
    """
    Convierte tokens a IDs numéricos según el .inf
    id=0, *=1, +=2, $=3
    """
    resultado = []

    for lexema, tipo, valor in tokens:
        if tipo == "IDENTIFICADOR":
            resultado.append(0)
        elif lexema == "*":
            resultado.append(1)
        elif lexema == "+":
            resultado.append(2)
        elif lexema == "$":
            resultado.append(3)

    return resultado


def parser_lr(tokens, archivo_lr):
    id_regla, lon_regla, nombre_regla, tabla = cargar_lr(archivo_lr)

    pila = [0]
    entrada = tokens.copy()
    paso = 1

    print("\nANÁLISIS SINTÁCTICO\n")

    while True:
        estado = pila[-1]

        if not entrada:
            print("❌ ERROR: entrada vacía")
            return

        simbolo = entrada[0]

        accion = tabla[estado][simbolo]

        print(f"Paso {paso}")
        print(f"Pila: {pila}")
        print(f"Entrada: {entrada}")

        # ERROR
        if accion == 0:
            print("❌ ERROR SINTÁCTICO")
            return

        # SHIFT
        elif accion > 0:
            pila.append(simbolo)
            pila.append(accion)
            entrada.pop(0)

            print(f"SHIFT -> estado {accion}\n")

        # REDUCE
        elif accion < 0:
            regla = -accion

            print(f"REDUCE R{regla}")

            for _ in range(lon_regla[regla - 1] * 2):
                pila.pop()

            estado = pila[-1]

            col_nt = id_regla[regla - 1]
            nuevo_estado = tabla[estado][col_nt]

            pila.append(nombre_regla[regla - 1])
            pila.append(nuevo_estado)

            print(f"Pila: {pila}\n")

            # ACEPTACIÓN
            if entrada[0] == 3 and len(pila) == 3:
                print("✅ CADENA ACEPTADA")
                return

        paso += 1