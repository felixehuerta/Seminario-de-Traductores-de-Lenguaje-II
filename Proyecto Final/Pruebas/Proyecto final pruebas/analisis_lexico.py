
import re


class AnalizadorLexico:

    def __init__(self):

        self.palabras_reservadas = {
            "if",
            "else",
            "while",
            "for",
            "int",
            "float",
            "char",
            "return",
            "void"
        }

        self.especificaciones = [
            ("NUMERO_REAL", r"\d+\.\d+"),
            ("NUMERO_ENTERO", r"\d+"),
            ("STRING", r'"[^"]*"'),
            ("IDENTIFICADOR", r"[a-zA-Z_][a-zA-Z0-9_]*"),
            ("OPERADOR", r"==|!=|<=|>=|\+|\-|\*|\/|=|<|>"),
            ("SIMBOLO", r"[(){};,]"),
            ("ESPACIO", r"\s+"),
            ("COMENTARIO", r"//.*?$|/\*.*?\*/"),
        ]

    def analizar(self, codigo):

        tokens = []

        patron_general = "|".join(
            f"(?P<{nombre}>{patron})"
            for nombre, patron in self.especificaciones
        )

        regex = re.compile(
            patron_general,
            re.DOTALL | re.MULTILINE
        )

        for match in regex.finditer(codigo):

            tipo = match.lastgroup
            lexema = match.group()

            if tipo in ("ESPACIO", "COMENTARIO"):
                continue

            if tipo == "IDENTIFICADOR":
                if lexema in self.palabras_reservadas:
                    tipo = "PALABRA_RESERVADA"

            tokens.append({
                "lexema": lexema,
                "tipo": tipo
            })

        return tokens
