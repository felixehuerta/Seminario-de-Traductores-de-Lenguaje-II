class Analisis_Semantico:

    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0
        self.errors = []
        self.variables = {}

    def token_actual(self):
        if self.token_index < len(self.tokens):
            return self.tokens[self.token_index]
        return None

    def avanzar(self):
        self.token_index += 1

    def analyze(self):

        while self.token_index < len(self.tokens):

            token = self.token_actual()

            if token[0] == "Tipo_dato":
                self.analizar_declaracion()

            elif token[0] == "Identificador":
                self.analizar_asignacion()

            else:
                self.avanzar()

        if not self.errors:
            return "Análisis semántico completado sin errores."

        return "\n".join(self.errors)

    def analizar_declaracion(self):

        tipo = self.token_actual()[1]
        linea = self.token_actual()[2]

        self.avanzar()

        if self.token_actual() and self.token_actual()[0] == "Identificador":

            nombre = self.token_actual()[1]

            if nombre in self.variables:
                self.errors.append(
                    f"Error semántico línea {linea}: variable '{nombre}' redeclarada"
                )
            else:
                self.variables[nombre] = tipo

            self.avanzar()

        else:
            self.errors.append(
                f"Error semántico línea {linea}: identificador esperado"
            )

    def analizar_asignacion(self):

        nombre = self.token_actual()[1]
        linea = self.token_actual()[2]

        if nombre not in self.variables:
            self.errors.append(
                f"Error semántico línea {linea}: variable '{nombre}' no declarada"
            )

        self.avanzar()

        if self.token_actual() and self.token_actual()[0] == "Op_asignacion":

            self.avanzar()

            if self.token_actual():

                valor = self.token_actual()

                if valor[0] == "Identificador":

                    if valor[1] not in self.variables:
                        self.errors.append(
                            f"Error semántico línea {linea}: variable '{valor[1]}' no declarada"
                        )

        while self.token_actual() and self.token_actual()[0] != "Punto_y_coma":
            self.avanzar()

        if self.token_actual():
            self.avanzar()


def analizar_semantica(tokens):
    analizador = Analisis_Semantico(tokens)
    return analizador.analyze()