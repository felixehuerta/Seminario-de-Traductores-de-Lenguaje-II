# ===============================
# MINI LENGUAJE C - COMPILADOR
# Léxico + Sintáctico + Semántico + Intérprete
# ===============================

import re

# ===============================
# ANALIZADOR LÉXICO
# ===============================

TOKENS = [
    ("INT", r'int\b'),
    ("FLOAT", r'float\b'),
    ("IF", r'if\b'),

    ("NUMBER", r'\d+(\.\d+)?'),
    ("ID", r'[a-zA-Z_]\w*'),

    ("EQ", r'=='),
    ("ASSIGN", r'='),
    ("GT", r'>'),
    ("LT", r'<'),

    ("PLUS", r'\+'),
    ("MINUS", r'-'),
    ("MUL", r'\*'),
    ("DIV", r'/'),

    ("LPAREN", r'\('),
    ("RPAREN", r'\)'),

    ("LBRACE", r'\{'),
    ("RBRACE", r'\}'),

    ("SEMI", r';'),

    ("SKIP", r'[ \t\n]+'),
]

def lexer(code):

    pos = 0
    tokens = []

    while pos < len(code):

        match = None

        for token, pattern in TOKENS:

            regex = re.compile(pattern)
            match = regex.match(code, pos)

            if match:

                text = match.group(0)

                if token != "SKIP":
                    tokens.append((token, text))

                pos = match.end()
                break

        if not match:
            raise Exception(f"Error léxico en: {code[pos]}")

    return tokens


# ===============================
# TABLA DE SÍMBOLOS
# ===============================

class SymbolTable:

    def __init__(self):
        self.symbols = {}

    def declare(self, name, type_):

        if name in self.symbols:
            raise Exception(f"Variable '{name}' ya declarada")

        self.symbols[name] = {
            "type": type_,
            "value": None
        }

    def set(self, name, value):

        if name not in self.symbols:
            raise Exception(f"Variable '{name}' no declarada")

        self.symbols[name]["value"] = value

    def get(self, name):

        if name not in self.symbols:
            raise Exception(f"Variable '{name}' no declarada")

        value = self.symbols[name]["value"]

        if value is None:
            raise Exception(f"Variable '{name}' sin inicializar")

        return value

    def get_type(self, name):

        if name not in self.symbols:
            raise Exception(f"Variable '{name}' no declarada")

        return self.symbols[name]["type"]


# ===============================
# ANALIZADOR SINTÁCTICO
# ===============================

class Parser:

    def __init__(self, tokens):

        self.tokens = tokens
        self.pos = 0

        self.symbols = SymbolTable()


    # -------------------------
    # UTILIDADES
    # -------------------------

    def current(self):
        return self.tokens[self.pos]

    def eat(self, token_type):

        if self.current()[0] == token_type:
            self.pos += 1
        else:
            raise Exception(
                f"Error sintáctico: se esperaba {token_type}"
            )


    # -------------------------
    # PROGRAMA
    # -------------------------

    def parse(self):

        while self.pos < len(self.tokens):
            self.statement()

        print("\n Programa ejecutado correctamente")


    # -------------------------
    # STATEMENTS
    # -------------------------

    def statement(self):

        token = self.current()[0]

        if token in ("INT", "FLOAT"):
            self.declaration()

        elif token == "ID":
            self.assignment()

        elif token == "IF":
            self.if_statement()

        else:
            raise Exception("Sentencia inválida")


    # -------------------------
    # DECLARACIÓN
    # -------------------------

    def declaration(self):

        type_ = self.current()[0].lower()
        self.eat(self.current()[0])

        name = self.current()[1]
        self.eat("ID")

        self.eat("SEMI")

        self.symbols.declare(name, type_)


    # -------------------------
    # ASIGNACIÓN
    # -------------------------

    def assignment(self):

        name = self.current()[1]
        self.eat("ID")

        self.eat("ASSIGN")

        value = self.expression()

        self.eat("SEMI")

        var_type = self.symbols.get_type(name)

        # Conversión de tipo
        if var_type == "int":
            value = int(value)

        if var_type == "float":
            value = float(value)

        self.symbols.set(name, value)


    # -------------------------
    # IF
    # -------------------------

    def if_statement(self):

        self.eat("IF")
        self.eat("LPAREN")

        condition = self.condition()

        self.eat("RPAREN")
        self.eat("LBRACE")

        if condition:

            while self.current()[0] != "RBRACE":
                self.statement()

        else:
            # Saltar bloque
            depth = 1

            while depth > 0:

                self.pos += 1

                if self.tokens[self.pos][0] == "LBRACE":
                    depth += 1

                if self.tokens[self.pos][0] == "RBRACE":
                    depth -= 1

        self.eat("RBRACE")


    # -------------------------
    # CONDICIÓN
    # -------------------------

    def condition(self):

        left = self.expression()

        op = self.current()[0]
        self.eat(op)

        right = self.expression()

        if op == "GT":
            return left > right

        if op == "LT":
            return left < right

        if op == "EQ":
            return left == right


    # -------------------------
    # EXPRESIONES
    # -------------------------

    def expression(self):

        value = self.term()

        while self.current()[0] in ("PLUS", "MINUS"):

            if self.current()[0] == "PLUS":
                self.eat("PLUS")
                value += self.term()

            else:
                self.eat("MINUS")
                value -= self.term()

        return value


    def term(self):

        value = self.factor()

        while self.current()[0] in ("MUL", "DIV"):

            if self.current()[0] == "MUL":
                self.eat("MUL")
                value *= self.factor()

            else:
                self.eat("DIV")
                value /= self.factor()

        return value


    def factor(self):

        token, value = self.current()

        if token == "NUMBER":

            self.eat("NUMBER")
            return float(value)

        if token == "ID":

            self.eat("ID")
            return self.symbols.get(value)

        if token == "LPAREN":

            self.eat("LPAREN")
            result = self.expression()
            self.eat("RPAREN")

            return result

        raise Exception("Factor inválido")


# ===============================
# MAIN
# ===============================

def run(code):

    print("=== CÓDIGO FUENTE ===")
    print(code)

    tokens = lexer(code)

    print("\n=== TOKENS ===")
    for t in tokens:
        print(t)

    parser = Parser(tokens)
    parser.parse()

    print("\n=== TABLA DE SÍMBOLOS ===")
    for k, v in parser.symbols.symbols.items():
        print(k, "=>", v)


if __name__ == "__main__":

    code = """
    int x;
    float y;

    x = 10;
    y = x * 2.5;

    if (y > 20) {
        x = x + 5;
    }

    print(x);
    """

    run(code)
