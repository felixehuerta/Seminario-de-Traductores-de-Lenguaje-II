import re   

tokens = [
    ('Libreria', r'#include\s+["<].*?[">]'),
    #Palabras reservadas
    ('Reservada_if', r'if'),
    ('Reservada_void', r'void'),
    ('Reservada_while', r'while'),
    ('Reservada_return', r'return'),
    ('Reservada_else', r'else'),
    #Nombre de variables, constantes, nomres de funcion
    ('Tipo_dato', r'\b(?:int|char|float|double|long|short|void)\b'),
    ('Identificador', r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'),    
    ('Cadena', r'"[^"]*"'),
    #Numeros 
    ('Real', r'\b[-+]?[0-9]*\.?[0-9]+\b'),
    ('Entero', r'\b\-?\d+\b'),    
    #Op para operaciones
    ('Op_adicion', r'[+\-]'),
    ('Op_multiplicacion', r'[*/]'),
    ('Op_asignacion', r'\='), 
    ('Op_relacional', r'[<>]=?|!=|=='),
    #Op boleanos
    ('Op_binario', r'and|&&|or|\|\|'),
    #Delimitadores
    ('Parentesis_apertura', r'\('),
    ('Parentesis_cierre', r'\)'),
    ('Llave_apertura', r'\{'),
    ('Llave_cierre', r'\}'),
    ('Punto_y_coma', r';'),
    ('Coma', r','),
    
    #ESPACIOS/FIN DE LINEA (SE OMITEN)
    ('Espacio', r'\s+')
]

def analizar(codigo):    #ANALISIS LEXICO: DEVOLVER TOKENS Y LEXEMAS
    resultados = []
    num=1                       #numero del token

    while codigo:               #Repasar el texto de entrada caracter por caracter
        encontrado = False      #bandera

        #Repasar lista de tokens y patrones del archivo tokenList.py                          
        for token_nombre, patron in tokens:                 
            coincidencia = re.match(patron, codigo)         #Revisar si algun patron coincide con el codigo leido
            if coincidencia:                                #El primer patron que coincide con la secuencia actual                          
                valor = coincidencia.group(0)
                for i in valor:
                    if i =="\n":
                        num+=1
                if token_nombre!="Espacio":                 #ignorar los espacios entre lexemas y reemplazar espacios dentro de un mismo lexema   
                    valor = valor.replace(" ", "_")         
                    resultados.append(
                        token_nombre + " " + valor + " " + str(num)
                        )
                codigo = codigo[len(valor):]                #Ir "eliminando" el codigo conforme lo analicemos
                encontrado = True                           #Alzar la bandera 
                break

        #En caso de que un token no forme parte de la gramatica (error lexico)
        if not encontrado:                                  
            token_incorrecto = ""
            for letra in codigo:
                token_incorrecto += letra
                if letra == " " or letra == "\n":
                    break
            return "Error: Token no válido en el código fuente -> " + token_incorrecto
        
    #Devolver resultados del analisis
    return resultados