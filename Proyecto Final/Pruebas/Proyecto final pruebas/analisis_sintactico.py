
class AnalizadorSintactico:

    def __init__(self, tokens):

        self.tokens = tokens
        self.posicion = 0

    def token_actual(self):

        if self.posicion < len(self.tokens):
            return self.tokens[self.posicion]

        return None

    def avanzar(self):
        self.posicion += 1

    def analizar(self):

        errores = []
        arbol = "Program\n"

        balance_parentesis = 0
        balance_llaves = 0

        for token in self.tokens:

            lexema = token["lexema"]

            if lexema == "(":
                balance_parentesis += 1

            elif lexema == ")":
                balance_parentesis -= 1

            elif lexema == "{":
                balance_llaves += 1

            elif lexema == "}":
                balance_llaves -= 1

            if balance_parentesis < 0:
                errores.append("Error sintáctico: ')' inesperado")

            if balance_llaves < 0:
                errores.append("Error sintáctico: '}' inesperado")

        if balance_parentesis != 0:
            errores.append(
                "Error sintáctico: paréntesis desbalanceados"
            )

        if balance_llaves != 0:
            errores.append(
                "Error sintáctico: llaves desbalanceadas"
            )

        for i, token in enumerate(self.tokens):

            if token["lexema"] == "if":

                if i + 1 >= len(self.tokens):
                    errores.append(
                        "Error sintáctico: falta condición después de if"
                    )

                elif self.tokens[i + 1]["lexema"] != "(":
                    errores.append(
                        "Error sintáctico: se esperaba '(' después de if"
                    )

        if errores:
            resultado = "\n".join(errores)
        else:
            resultado = "Análisis sintáctico completado correctamente.\n"

        arbol += " ├── Declaraciones\n"
        arbol += " ├── Expresiones\n"
        arbol += " └── Bloques\n"

        return resultado, arbol
