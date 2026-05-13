
# Compilador Básico de Lenguaje C

El **Compilador Básico de Lenguaje C** es una aplicación de escritorio desarrollada en Python que simula las principales fases de un compilador tradicional para el lenguaje de programación C. 

El proyecto proporciona una interfaz gráfica intuitiva que permite escribir, cargar, analizar y validar código fuente mediante análisis léxico, sintáctico y semántico.

Este compilador fue diseñado con fines educativos y prácticos, demostrando conceptos fundamentales de teoría de compiladores, autómatas finitos, generación de tokens, validación gramatical y construcción de árboles sintácticos.

El sistema utiliza un archivo `.lr` antes de iniciar la ejecución, el cual contiene las reglas gramaticales y transiciones utilizadas durante el proceso de compilación, funcionando de manera similar a las reglas de un autómata finito.

Al finalizar el proceso, el sistema genera:

- Resultado del análisis léxico
- Resultado del análisis sintáctico
- Resultado del análisis semántico
- Árbol sintáctico generado

Todo el proceso se encuentra integrado en una interfaz gráfica amigable e interactiva.

------------------------------------------------------------

# Arquitectura del Proyecto

El compilador está dividido en cuatro módulos principales escritos en Python.

------------------------------------------------------------

## 1. Main.py

`Main.py` funciona como el núcleo principal del proyecto y controla toda la ejecución del compilador.

Responsabilidades principales:

- Inicializar la interfaz gráfica
- Coordinar la comunicación entre módulos
- Ejecutar el flujo de compilación
- Cargar archivos `.lr`
- Mostrar resultados de análisis
- Gestionar interacción con el usuario
- Administrar entrada y salida de archivos

Este módulo conecta todas las fases del compilador en un único flujo de ejecución.

------------------------------------------------------------

## 2. Analisis_Lexico.py

El analizador léxico es responsable de leer el código fuente y convertirlo en tokens.

Funciones principales:

- Reconocimiento de palabras reservadas
- Identificación de variables
- Reconocimiento de números enteros y reales
- Detección de cadenas de texto
- Reconocimiento de operadores y símbolos
- Eliminación de comentarios y espacios innecesarios
- Generación de tabla de tokens

Ejemplo:

if (x > 10)

Tokens generados:

| Lexema | Tipo |
|--------|------|
| if | Palabra Reservada |
| ( | Símbolo |
| x | Identificador |
| > | Operador |
| 10 | Número Entero |
| ) | Símbolo |

El análisis léxico representa la primera fase del compilador.

------------------------------------------------------------

## 3. Analisis_Sintactico.py

El analizador sintáctico verifica que la secuencia de tokens cumpla correctamente las reglas gramaticales del lenguaje.

Responsabilidades:

- Validar el orden de los tokens
- Aplicar reglas de producción
- Detectar errores sintácticos
- Construir estructuras de análisis
- Generar el árbol sintáctico

Ejemplo:

if x > 10

Resultado:

Error Sintáctico: Se esperaba '(' después de 'if'

El parser utiliza las reglas definidas dentro del archivo `.lr`.

------------------------------------------------------------

## 4. Analisis_Semantico.py

El analizador semántico valida la coherencia lógica del programa después del análisis sintáctico.

Responsabilidades:

- Verificar declaraciones de variables
- Validar compatibilidad de tipos
- Detectar variables no declaradas
- Evitar operaciones inválidas
- Validar asignaciones
- Detectar inconsistencias semánticas

Ejemplo:

int x = "Hola";

Resultado:

Error Semántico: No se puede asignar una cadena a una variable entera

Esta fase garantiza que el código tenga sentido lógico además de cumplir las reglas gramaticales.

------------------------------------------------------------

# Archivo LR

Antes de iniciar el compilador, el sistema carga un archivo `.lr` que contiene:

- Reglas gramaticales
- Tabla de transiciones
- Configuración del parser
- Reglas del autómata finito

Este archivo permite simular el comportamiento de compiladores profesionales basados en autómatas y análisis LR.

------------------------------------------------------------

# Características Principales

## Análisis Léxico

- Generación de tokens
- Reconocimiento de palabras reservadas
- Validación de identificadores
- Reconocimiento de números
- Detección de cadenas
- Eliminación de comentarios

------------------------------------------------------------

## Análisis Sintáctico

- Validación gramatical
- Construcción del parser
- Detección de errores sintácticos
- Generación del árbol sintáctico
- Interpretación de reglas LR

------------------------------------------------------------

## Análisis Semántico

- Validación de tipos de datos
- Verificación de declaraciones
- Control de variables
- Detección de errores lógicos
- Reporte de inconsistencias semánticas

------------------------------------------------------------

## Generación de Árbol Sintáctico

El compilador genera un árbol sintáctico que representa gráficamente la estructura del programa analizado.

------------------------------------------------------------

## Interfaz Gráfica

La aplicación incluye una interfaz gráfica completa donde el usuario puede:

- Escribir código fuente
- Abrir archivos `.c`
- Ejecutar compilación
- Visualizar tokens
- Mostrar árbol sintáctico
- Consultar errores
- Ver resultados de análisis en tiempo real

------------------------------------------------------------

# Tecnologías Utilizadas

El proyecto fue desarrollado utilizando las siguientes tecnologías:

- Python
- Tkinter / PyQt
- Técnicas de Parsing LR
- Conceptos de Autómatas Finitos
- Teoría de Compiladores

------------------------------------------------------------

# Requisitos Previos

Antes de ejecutar el proyecto es necesario tener instalado:

- Python 3.10 o superior
- pip
- Librerías necesarias del proyecto

------------------------------------------------------------

# Instalación

## Clonar el repositorio

git clone https://github.com/your-user/basic-c-compiler.git

## Entrar al directorio

cd basic-c-compiler

## Ejecutar el proyecto

python Main.py

------------------------------------------------------------

# Estructura del Proyecto

basic-c-compiler/
│
├── Main.py
├── Analisis_Lexico.py
├── Analisis_Sintactico.py
├── Analisis_Semantico.py
├── reglas.lr
└── README.txt

------------------------------------------------------------

# Flujo de Compilación

El compilador ejecuta las siguientes etapas:

1. Cargar archivo LR
2. Leer código fuente
3. Realizar análisis léxico
4. Generar tokens
5. Ejecutar análisis sintáctico
6. Construir árbol sintáctico
7. Ejecutar análisis semántico
8. Mostrar resultados en interfaz gráfica

------------------------------------------------------------

# Ejemplo de Ejecución

## Código Fuente

int x = 10;

if(x > 5){
    x = x + 1;
}

## Resultado del Compilador

### Análisis Léxico

TOKEN: int -> Palabra Reservada
TOKEN: x -> Identificador
TOKEN: = -> Operador de Asignación
TOKEN: 10 -> Número Entero

### Análisis Sintáctico

Análisis sintáctico completado correctamente.

### Análisis Semántico

Análisis semántico completado correctamente.

### Árbol Sintáctico

Program
 └── IfStatement
      ├── Condition
      └── Block

------------------------------------------------------------

# Objetivo Educativo

Este proyecto fue desarrollado principalmente con fines educativos para demostrar de manera práctica el funcionamiento interno de un compilador.

Puede ser utilizado en:

- Cursos de compiladores
- Materias de autómatas
- Demostraciones de parsing
- Investigación académica
- Proyectos universitarios

------------------------------------------------------------

# Mejoras Futuras

Características planeadas para futuras versiones:

- Generación de código intermedio
- Generación de código ensamblador
- Optimización de código
- Soporte para funciones y arreglos
- Manejo avanzado de scopes
- Recuperación de errores
- Exportación de árboles sintácticos
- Compilación multifile

------------------------------------------------------------

# Licencia

El software puede ser utilizado, modificado y distribuido libremente con fines educativos y personales.

El proyecto se proporciona "tal cual", sin garantías de ningún tipo.
