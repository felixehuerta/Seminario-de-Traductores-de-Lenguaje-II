class Analisis_Semantico:
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.i = 0
        self.variables = set()
        self.errores = []

    def analizar(self):
        while self.i < len(self.tokens):
            token = self.tokens[self.i]

            if token[0] == "Tipo_dato":
                self.declarar()

            elif token[0] == "Identificador":
                self.usar()

            else:
                self.i += 1

        if not self.errores:
            return "Analisis semantico correcto."
        return "\n".join(self.errores)

    def declarar(self):
        self.i += 1
        if self.tokens[self.i][0] == "Identificador":
            var = self.tokens[self.i][1]
            self.variables.add(var)
        self.i += 1

    def usar(self):
        var = self.tokens[self.i][1]
        if var not in self.variables:
            self.errores.append(f"Variable '{var}' no declarada")
        self.i += 1

def analizar_semantica(tokens):
    return Analisis_Semantico(tokens).analizar()