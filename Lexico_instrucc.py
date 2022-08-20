from Token import Token
from TypeToken import TypeToken


class Lexico_instrucciones():
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

    nombre_grafica = ''
    tipo_grafica = ''
    titulo = ''
    titulo_x = ''
    tirulo_y = ''
    lista_tokens = []

    def __init__(self,palabra):
        self.estado = 0
        self.lexema = ''
        self.tokens= []
        palabra = palabra + "@"
        actual_p = ''
        longitud_p = len(palabra)

        for i in range(longitud_p):
            actual_p = palabra[i]

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
                elif actual_p == '<':
                    self.lexema += actual_p
                    self.AgregarToken(TypeToken.MENOR_QUE.name)
                    continue
                elif actual_p == '>':
                    self.lexema += actual_p
                    self.AgregarToken(TypeToken.MAYOR_QUE.name)
                    continue
                elif actual_p == '¿':
                    self.lexema += actual_p
                    self.AgregarToken(TypeToken.INTERROGACION_ABRE.name)
                    continue
                elif actual_p == '?':
                    self.lexema += actual_p
                    self.AgregarToken(TypeToken.INTERROGACION_CIERRA.name)
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
                        if actual_p == ':':
                            self.lexema += actual_p
                            self.AgregarToken(TypeToken.DOS_PUNTOS.name)
                            continue
                        i =- 1
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
            if self.estado == 4:
                if actual_p.isdigit():
                    self.estado = 4
                    self.lexema += actual_p
                    continue
                else:
                    self.AgregarToken(TypeToken.NUMERO.name)
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
        if palabra =='NOMBRE':
            self.tipo = TypeToken.NOMBRE  #Mejor control
            return True
        if palabra == 'GRAFICA':
            self.tipo = TypeToken.GRAFICA #Mejor control
            return True
        if palabra == 'TITULO':
            self.tipo = TypeToken.TITULO #Mejor control
            return True
        if palabra == 'TITULOX':
            self.tipo = TypeToken.TITULOX #Mejor control
            return True
        if palabra == 'TITULOY':
            self.tipo = TypeToken.TITULOY #Mejor control
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