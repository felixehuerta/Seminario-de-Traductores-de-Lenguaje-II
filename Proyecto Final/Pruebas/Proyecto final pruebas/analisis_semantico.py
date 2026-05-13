
class AnalizadorSemantico:

    def __init__(self, tokens):

        self.tokens = tokens
        self.variables = {}

    def analizar(self):

        errores = []

        tipos_validos = {
            "int",
            "float",
            "char"
        }

        i = 0

        while i < len(self.tokens):

            token = self.tokens[i]

            # Declaración de variables
            if token["lexema"] in tipos_validos:

                if i + 1 < len(self.tokens):

                    siguiente = self.tokens[i + 1]

                    if siguiente["tipo"] == "IDENTIFICADOR":

                        nombre_variable = siguiente["lexema"]
                        tipo_variable = token["lexema"]

                        self.variables[nombre_variable] = tipo_variable

                        # Validar asignación
                        if i + 3 < len(self.tokens):

                            operador = self.tokens[i + 2]["lexema"]
                            valor = self.tokens[i + 3]

                            if operador == "=":

                                if (
                                    tipo_variable == "int"
                                    and valor["tipo"] == "STRING"
                                ):
                                    errores.append(
                                        f"Error semántico: "
                                        f"No se puede asignar STRING "
                                        f"a variable int '{nombre_variable}'"
                                    )

                                if (
                                    tipo_variable == "char"
                                    and valor["tipo"] == "NUMERO_ENTERO"
                                ):
                                    errores.append(
                                        f"Error semántico: "
                                        f"No se puede asignar entero "
                                        f"a variable char '{nombre_variable}'"
                                    )

            # Uso de variables no declaradas
            if token["tipo"] == "IDENTIFICADOR":

                nombre = token["lexema"]

                anterior = (
                    self.tokens[i - 1]["lexema"]
                    if i > 0 else ""
                )

                if anterior not in tipos_validos:

                    if nombre not in self.variables:
                        errores.append(
                            f"Error semántico: "
                            f"Variable '{nombre}' no declarada"
                        )

            i += 1

        if errores:
            return "\n".join(set(errores))

        return "Análisis semántico completado correctamente."
