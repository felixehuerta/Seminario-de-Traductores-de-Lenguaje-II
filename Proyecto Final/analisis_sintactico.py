class manageTokens: #CLASE AUXILIAR PARA DEVOLVER TOKENS DESDE EL ARCHIVO DE SALIDA

    def __init__(self) -> None:

        with open("tokens.txt", "r", encoding='utf-8') as file:
            self.tokens = file.readlines()
            self.total = self.tokens.__len__()
            if (self.total == 0):
                raise ValueError("No hay tokens que analizar")
        self.i = 0

    #Devolver el nombre de los tokens
        
    def actual(self):
        try:
            cadena = (self.tokens[self.i]).split()
        except:
            return ""
        token = cadena[0]
        return token
    
    def siguiente(self):
        try:
            cadena = (self.tokens[self.i+1]).split()
        except:
            return ""
        token = cadena[0] 
        return token
    
    #Avanzar y retroceder lista de tokens
    #Pero tambien devuelve el nombre de los tokens
  
    def avanzar(self, n=1):
        if self.i < self.total:
            self.i+=n
            return self.actual()
        return ""
    
    def retroceder(self, n=1):
        if self.i > 0:
            self.i-=n
            return self.actual()
        return ""

    #Para comparaciones sencillas

    def es_actual(self, nombreToken):
        return nombreToken==self.actual()
    
    def es_siguiente(self, nombreToken):
        return nombreToken==self.siguiente()
    
    #Devolver la linea de codigo correspondiente al token

    def linea_token_actual(self):
        try:
            cadena = (self.tokens[self.i]).split()
            return cadena[2]
        except:
            return "-1"

    def linea_token_siguiente(self):
        try:
            cadena = (self.tokens[self.i + 1]).split()
            return cadena[2]
        except:
            return "-1"
    
    def lexema_actual(self):
        try:
            cadena = (self.tokens[self.i]).split()
            return cadena[1]
        except:
            return "Fuera de limites"
    
    def lexema_siguiente(self):
        try:
            cadena = (self.tokens[self.i+1]).split()
            return cadena[1]
        except:
            return "Fuera de limites"



#IMPLEMENTACION DE LAS REGLAS DE PRODUCCION, SE ANALIZAN LAS SECUENCIAS DE TOKENS 

t = manageTokens()
mensaje = ""


def VALOR():        #RECONOCE VARIABLES Y NUMEROS
    if t.es_actual("Entero") or t.es_actual("Real") or t.es_actual("Identificador"):
        t.avanzar()
        return True
    else:
        return False

def OPERACION():    #RECONOCE OPERACIONES SIMPLES SIN PARENTESIS: SUMA, RESTA, MULTIPLICACION 
    if (VALOR()):
        if t.es_actual("Op_adicion") or t.es_actual("Op_multiplicacion"):
            t.avanzar()
            if VALOR():
                if not t.es_actual("Op_adicion") and not t.es_actual("Op_multiplicacion"):
                    return True
                else:
                    t.retroceder()
                    return OPERACION()
            else:
                t.retroceder(2)
                return False
        else:
            t.retroceder()
            return False
    else:
        return False

def EXPRESION():    #RECONOCE OPERACIONES, NUMEROS O VARIABLES 
    if OPERACION():
        return True
    elif VALOR():
        return True
    elif t.es_actual("Cadena"):
        t.avanzar()
        return True
    return False

def COMPARACION():  #RECONOCE COMPRACIONES ENTRE NUMEROS VARIABLES U OPERACIONES
    if EXPRESION():
        if t.es_actual("Op_relacional"):
            t.avanzar()
            if EXPRESION():
                return True
            t.retroceder(2)
    return False

def ASIGNACION():   #RECONOCE ASIGNACIONES DE UN VALOR A UNA VARIABLE O DE UNA VARIABLE A OTRA
    if t.es_actual("Identificador") and t.es_siguiente("Op_asignacion"):
        t.avanzar(2)
        
        if t.es_actual("Identificador") and t.es_siguiente("Punto_y_coma"):
            t.avanzar(2)
            return True
        elif EXPRESION():
            if t.es_actual("Punto_y_coma"):
                t.avanzar()
                return True  
            else:
                t.retroceder()  
        t.retroceder(2)
    return False

def DECLARACION():  #RECONOCE DECLARACIONES DE VARIABLES SIMPLES O CON UNA OPERACION
    if t.es_actual("Tipo_dato"):
        t.avanzar()
        if t.es_actual("Identificador") and t.es_siguiente("Punto_y_coma"):
            t.avanzar(2)
            return True
        elif ASIGNACION():
            return True
        t.retroceder()
    return False

def PARAMETROS():   #SOLO CONSIDERA QUE SI HAYA PARAMETROS, POR PROBAR
    if t.es_actual("Tipo_dato"):
        t.avanzar()
        #Caso base, un solo parametro
        if t.es_actual("Identificador") and not t.es_siguiente("Coma"):
            t.avanzar()
            return True
        #Caso recursivo, varios parametros
        elif t.es_actual("Identificador") and t.es_siguiente("Coma"):
            t.avanzar(2)
            if PARAMETROS():
                return True
            else:
                t.retroceder(2)
                return False
        else:
            t.retroceder()
    return False

def IF():           #SOLO RECONOCE IF SIMPLES, NO ELSE IF, ELSE ...
    if t.es_actual("Reservada_if") and t.es_siguiente("Parentesis_apertura"):
        t.avanzar(2)
        
        bandera = False

        if COMPARACION() and t.es_actual("Parentesis_cierre"):
            bandera = True
        
        if VALOR() and t.es_actual("Parentesis_cierre"):
            bandera = True

        if bandera:
            t.avanzar()
            return BLOQUE()

    return False

def BLOQUE():       #IMPORTANTE: RECONOCE BLOQUES DE CODIGO -> {instrucciones}
    global mensaje

    llaves=0        #verificar que las llaves esten correctamente anidadas

    if t.es_actual("Llave_apertura") and t.es_siguiente("Llave_cierre"):
        return True
    
    elif t.es_actual("Llave_apertura") and not t.es_siguiente("Llave_cierre"):
        llaves += 1
        t.avanzar()

        while (True):
            correcto = False #verificar que el codigo leido sea correcto
            linea = t.linea_token_actual()

            if t.es_actual(""):
                if  llaves != 0:
                    mensaje = "Llaves mal indentadas"
                    return False
                else:
                    return True

            elif t.es_actual("Llave_cierre"):
                llaves-=1
                t.avanzar()
                if (llaves == 0):
                    return True
                elif (llaves < 0):
                    mensaje = "Llaves mal indentadas, " + linea
                    return False
                else:
                    correcto = True
                
            elif t.es_actual("Llave_apertura"):
                t.avanzar()
                llaves+=1
            
            elif ASIGNACION():
                correcto = True
            
            elif DECLARACION():
                correcto = True
            
            elif ENCABEZADO():
                correcto = True
            
            elif IF():
                correcto = True

            if not correcto:
                mensaje = "Error en la linea " + linea + ", " + t.lexema_actual()
                return False

    return False

def ENCABEZADO():   #RECONOCE SECUENCIAS DE ENCABEZADOS (#INCLUDE ...)
    if t.es_actual("Libreria")  and not t.es_siguiente("Libreria"):
        t.avanzar()
        return True
    elif t.es_actual("Libreria") and t.es_siguiente("Libreria"):
        t.avanzar()
        ENCABEZADO()
    else:
        return False

def FUNCION():
    if t.es_actual("Tipo_dato") and t.es_siguiente("Identificador"):
        t.avanzar(2)

        bandera = False

        if t.es_actual("Parentesis_apertura") and t.es_siguiente("Parentesis_cierre"):
            t.avanzar(2)
            bandera = True

        else:
            t.avanzar()
            if PARAMETROS() and t.es_actual("Parentesis_cierre"):
                t.avanzar()
                bandera = True

        if bandera:
            return BLOQUE()
        
        else:
            t.retroceder(3)
        
    return False


def Verificar(): #FUNCION PRINCIPAL, EMPLEA LAS OTRAS FUNCIONES PARA VERIFICAR QUE EL CODIGO PRINCIPALK SEA CORRECTO
    global mensaje
    mensaje = "Analisis sintactico correcto."
    while(True):
        correcto = False

        if t.actual()=="":
            break

        if ENCABEZADO():
            correcto = True

        elif FUNCION():
            correcto = True

        if not correcto:
            mensaje = "Error en la linea " + t.linea_token_actual() + ", " + t.lexema_actual()
            break

    return mensaje