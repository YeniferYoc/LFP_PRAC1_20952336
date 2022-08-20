from Token import Token
from TypeToken import TypeToken
from Producto import *


class Lexico_data():
    """
   CADENA = 2
    NUMERO = 3
    LLAVE_ABRE = 4
    LLAVE_CIERRA =5
    CORCHETE_ABRE = 6
    CORCHETE_CIERRE = 7
    PUNTO_COMA = 8
    COMA = 9
    DOS_PUNTOS =10
    DESCONOCIDO = 11
    NOMBRE = 12
    GRAFICA = 13
    LETRAS = 14
    PARENTESIS_ABRE = 15
    PARENTESIS_CIERRA = 16
    INTERROGACION_ABRE = 17
    INTERROGACION_CIERRA = 18
    MAYOR_QUE = 19
    MENOR_QUE = 20
    """
    
    tipo = TypeToken.DESCONOCIDO

    nombre_mes = ''
    año = 0
    arreglo_productos = []
    lista_tokens = []

    def __init__(self,entrada):
        self.estado = 0
        self.lexema = ''
        self.tokens= []
        entrada = entrada + "@"
        actual_p = ''
        longitud_p = len(entrada)

        for i in range(longitud_p):
            actual_p = entrada[i]

            if self.estado == 0:

                if actual_p.isalpha():
                    self.estado = 1
                    self.lexema += actual_p
                    continue
                elif actual_p.isdigit():
                    self.estado = 4
                    self.lexema += actual_p
                    continue
                elif actual_p == '"':
                    self.estado = 2
                    continue
                elif actual_p == '(':
                    self.lexema += actual_p
                    self.AgregarToken(TypeToken.PARENTESIS_ABRE.name)
                    continue
                elif actual_p == ')':
                    self.lexema += actual_p
                    self.AgregarToken(TypeToken.PARENTESIS_CIERRA.name)
                    continue
                elif actual_p == '[':
                    self.lexema += actual_p
                    self.AgregarToken(TypeToken.CORCHETE_ABRE.name)
                    continue
                elif actual_p == ']':
                    self.lexema += actual_p
                    self.AgregarToken(TypeToken.CORCHETE_CIERRE.name)
                    continue
                elif actual_p == '=':
                    self.lexema += actual_p
                    self.AgregarToken(TypeToken.IGUAL.name)
                    continue
                elif actual_p == ';':
                    self.lexema += actual_p
                    self.AgregarToken(TypeToken.PUNTO_COMA.name)
                    continue
                elif actual_p == ',':
                    self.lexema += actual_p
                    self.AgregarToken(TypeToken.COMA.name)
                    continue
                elif actual_p == ':':
                    self.lexema += actual_p
                    self.AgregarToken(TypeToken.DOS_PUNTOS.name)
                    continue
                elif actual_p =='@':
                    print( '********* ANALISIS INTRUCCIONES FINALIZADOS ***********')
                    continue
                elif actual_p == ' ' or actual_p =="\n" or actual_p == "\r" or actual_p =='\t':
                    self.estado = 0
                    continue
                else:
                    print("@@@@ ERROR: ", actual_p)
                    self.lexema = ''
                    continue
            # Estado para manejar letras
            if self.estado == 1:
                if actual_p.isalpha():
                    self.estado = 1
                    self.lexema += actual_p
                    continue
                else:
                    # Verificar si esta dentro de las palabras que solicitan
                    if self.Reservada():
                        self.AgregarToken(self.tipo.name)
                        print(actual_p)
                        print(i)
                        if actual_p == ':':
                            self.lexema += actual_p
                            self.AgregarToken(TypeToken.DOS_PUNTOS.name)
                            continue
                        i =- 1
                        print(i)
                        continue
                    else:
                        self.AgregarToken(TypeToken.LETRAS.name)
                        i -= 1
                        continue
            #Estado para manejar cadenas
            if self.estado == 2:
                if actual_p != '"':
                    self.estado = 2
                    self.lexema += actual_p
                    continue
                else:
                    self.estado = 3
                    self.AgregarToken(TypeToken.CADENA.name)
            #ESTADO PARA MANEJAR NUMEROS DECIMALES
            if self.estado == 4:
                if actual_p.isdigit():
                    self.estado = 4
                    self.lexema += actual_p
                    continue
                elif actual_p == '.':
                    self.lexema += actual_p
                    continue
                
                else:
                    self.AgregarToken(TypeToken.NUMERO.name)
                    if actual_p == ']':
                            self.lexema += actual_p
                            self.AgregarToken(TypeToken.CORCHETE_CIERRE.name)
                            continue
                    elif actual_p == ',':
                            self.lexema += actual_p
                            self.AgregarToken(TypeToken.COMA.name)
                            continue
                    i -= 1
                    continue
            



    def AgregarToken(self, tipo):
        self.tokens.append(Token(self.lexema, tipo))
        self.lista_tokens.append(Token(self.lexema, tipo))
        self.lexema =''
        self.estado = 0
        self.tipo = TypeToken.DESCONOCIDO

    def Reservada(self):
        palabra = self.lexema.upper()
        #lista_palabras = ['NOMBRE', 'GRAFICA']
        if palabra =='ENERO'or 'FEBRERO'or 'MARZO' or 'ABRIL' or 'MAYO' or 'JUNIO' or 'JULIO' or 'AGOSTO' or 'SEPTIEMBRE' or 'OCTUBRE'or 'NOVIEMBRE' or 'DICIEMBRE':
            self.tipo = TypeToken.NOMBRE_MES  #Mejor control
            return True
        if palabra == 'AÑO':
            self.tipo = TypeToken.AÑO #Mejor control
            return True

        return False

    def printTokens(self):
        for token in self.tokens:
            print(token.lexema + " -> Tipo: " + str(token.type))

    

    def GuardarDatos(self):
        longitud_p = len(self.tokens)
        for i in range(longitud_p):
            if self.tokens[i].type == TypeToken.NOMBRE.name:
                i = i + 2
                self.nombre_grafica = self.tokens[i].lexema

        print(self.nombre_grafica)