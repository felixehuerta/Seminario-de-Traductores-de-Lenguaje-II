class Analisis_Semantico:
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0
        self.errors = []

    def analyze(self):
        while self.token_index < len(self.tokens):
            if not self.declaracion():
                self.errors.append(f"Error semántico en línea {self.tokens[self.token_index][2]}: No se pudo analizar la declaración")
                break
        if not self.errors:
            return "Análisis semántico completado sin errores."
        else:
            return "\n".join(self.errors)

    def avanzar(self):
        self.token_index += 1

    def retroceder(self):
        self.token_index -= 1

    def token_actual(self):
        return self.tokens[self.token_index]

    def token_siguiente(self):
        if self.token_index + 1 < len(self.tokens):
            return self.tokens[self.token_index + 1]
        else:
            return None

    def declaracion(self):
        if self.token_actual()[0] == 'Tipo_dato':
            tipo_dato = self.token_actual()[1]
            self.avanzar()
            if self.token_actual()[0] == 'Identificador':
                variable = self.token_actual()[1]
                self.avanzar()
                if self.token_actual()[0] == 'Punto_y_coma':
                    self.avanzar()
                    return True
        return False

def analizar_semantica(tokens):
    semantic_analyzer = Analisis_Semantico(tokens)
    return semantic_analyzer.analyze()

    
