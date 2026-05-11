class manageTokens:

    def __init__(self) -> None:
        with open("tokens.txt", "r", encoding='utf-8') as file:
            self.tokens = file.readlines()
            self.total = len(self.tokens)
            if self.total == 0:
                raise ValueError("No hay tokens que analizar")
        self.i = 0

    def actual(self):
        try:
            return self.tokens[self.i].split()[0]
        except:
            return ""

    def siguiente(self):
        try:
            return self.tokens[self.i+1].split()[0]
        except:
            return ""

    def avanzar(self, n=1):
        self.i += n
        return self.actual()

    def retroceder(self, n=1):
        self.i -= n
        return self.actual()

    def es_actual(self, token):
        return token == self.actual()

    def es_siguiente(self, token):
        return token == self.siguiente()

    def linea_token_actual(self):
        try:
            return self.tokens[self.i].split()[2]
        except:
            return "-1"

    def lexema_actual(self):
        try:
            return self.tokens[self.i].split()[1]
        except:
            return "?"

t = None
mensaje = ""

def VALOR():
    if t.es_actual("Entero") or t.es_actual("Real") or t.es_actual("Identificador"):
        t.avanzar()
        return True
    return False

def EXPRESION():
    return VALOR()

def ASIGNACION():
    if t.es_actual("Identificador") and t.es_siguiente("Op_asignacion"):
        t.avanzar(2)
        if EXPRESION() and t.es_actual("Punto_y_coma"):
            t.avanzar()
            return True
    return False

def DECLARACION():
    if t.es_actual("Tipo_dato"):
        t.avanzar()
        if t.es_actual("Identificador") and t.es_siguiente("Punto_y_coma"):
            t.avanzar(2)
            return True
    return False

def BLOQUE():
    if t.es_actual("Llave_apertura"):
        t.avanzar()
        while not t.es_actual("Llave_cierre"):
            if not (DECLARACION() or ASIGNACION()):
                return False
        t.avanzar()
        return True
    return False

def FUNCION():
    if t.es_actual("Tipo_dato") and t.es_siguiente("Identificador"):
        t.avanzar(2)
        if t.es_actual("Parentesis_apertura"):
            while not t.es_actual("Parentesis_cierre"):
                t.avanzar()
            t.avanzar()
            return BLOQUE()
    return False

def ENCABEZADO():
    if t.es_actual("Libreria"):
        t.avanzar()
        return True
    return False

def Verificar():
    global t, mensaje
    t = manageTokens()
    mensaje = "Analisis sintactico correcto."

    while t.actual() != "":
        if not (ENCABEZADO() or FUNCION()):
            mensaje = "Error en linea " + t.linea_token_actual()
            break

    return mensaje