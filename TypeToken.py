from enum import Enum

class TypeToken(Enum):
    CADENA = 2
    NUMERO = 3
    NOMBRE_MES = 4
    AÑO =5
    CORCHETE_ABRE = 6
    CORCHETE_CIERRE = 7
    PUNTO_COMA = 8
    COMA = 9
    DOS_PUNTOS =10
    DESCONOCIDO = 11
    NOMBRE = 12
    GRAFICA = 13
    TITULO = 21
    TITULOX = 22
    TITULOY = 23
    IGUAL = 24
    PUNTO = 25
    LETRAS = 14
    PARENTESIS_ABRE = 15
    PARENTESIS_CIERRA = 16
    INTERROGACION_ABRE = 17
    INTERROGACION_CIERRA = 18
    MAYOR_QUE = 19
    MENOR_QUE = 20
