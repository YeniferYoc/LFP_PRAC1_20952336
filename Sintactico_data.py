from Token import Token
from TypeToken import TypeToken
from Producto import *

class Sintactico_data():
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

    nombre_mes = ''
    año_gra = 0
    arreglo_productos = []
    lista_tokens = []
    arreglo_lleno = []
    datos_generales = []



    def __init__(self,tokens):

        self.tokens= tokens
        longitud_arr = len(tokens)

        #prueba = []
        #prueba = self.Buscar_elemento(TypeToken.TITULO.name)
        #print(prueba[1]) no se encotnro, argumento devuelve none si no se encontro

        #arreglo_dos_puntos = self.Buscar_elemento(TypeToken.DOS_PUNTOS.name)
        for i in range(longitud_arr):# SE RECORRE LA LONGITUD DEL ARREGLO
                if self.tokens[i].type == TypeToken.NOMBRE_MES.name:
                    if self.tokens[i+1].type == TypeToken.DOS_PUNTOS.name:#SE VERIFICA QUE CUMPLA DETEMINDAMENTE CON CAMPO Y CON CONTENIDO
                        if self.tokens[i+2].type == TypeToken.NUMERO.name:
                            print("campo completo")
                            self.nombre_mes = self.tokens[i].lexema
                            self.año_gra = self.tokens[i+2].lexema
                            self.datos_generales.append(self.nombre_mes)
                            self.datos_generales.append(self.año_gra)
                            print(self.nombre_mes)
                            print(self.año_gra)
                        else:
                            print("SE ESPERABA EL AÑO")
                            
                            break
                    else:#SINO SE CUMPLE ENTONCES QUE SE ROMPA EL CICLO 
                        print("SE ESPERABAn DOS PUNTOS")
                        break
                    continue
        
        print(len(self.datos_generales))
        self.arreglo_productos = self.Buscar_elemento(TypeToken.CORCHETE_ABRE.name)
        
        for producto in self.arreglo_productos:
            print(producto.producto + " -> precio: " + str(producto.precio_u)+" ganancia: "+str(producto.ganancia))### aqui mi quede
        

        


    def Buscar_elemento(self, tipo):
        longitud_arr = len(self.tokens)
        for i in range(longitud_arr):# SE RECORRE LA LONGITUD DEL ARREGLO
                if self.tokens[i].type == tipo:
                    print("ENCONTRE CORCHETE ABRE")
                    if self.tokens[i+1].type == TypeToken.CADENA.name:#SE VERIFICA QUE CUMPLA DETEMINDAMENTE CON CAMPO Y CON CONTENIDO
                        print("ENCONTRE CADENA ")
                        if self.tokens[i+2].type == TypeToken.COMA.name:
                            print("ENCONTRE COMA")
                            if self.tokens[i+3].type == TypeToken.NUMERO.name:
                                print("ENCONTRE PRECIO")
                                if self.tokens[i+4].type == TypeToken.COMA.name:
                                    print("ENCONTRE COMA")
                                    if self.tokens[i+5].type == TypeToken.NUMERO.name:
                                        print("ENCONTRE CANTIDAD")
                                        if self.tokens[i+6].type == TypeToken.CORCHETE_CIERRE.name:
                                            print("ENCONTRE CORCHETE CIERRA")
                                            if self.tokens[i+7].type == TypeToken.PUNTO_COMA.name:
                                                print("ENCONTRE PUNTO Y COMA")
                                                print("campo completo")
                                                nombre_prod = self.tokens[i+1].lexema
                                                precio_prod = float(self.tokens[i+3].lexema)
                                                cant_ven = int(self.tokens[i+5].lexema)
                                                ganancia = float(precio_prod*cant_ven)
                                                producto_nuevo = Producto(nombre_prod, precio_prod, cant_ven, ganancia)
                                                self.arreglo_productos.append(producto_nuevo)

                                                print(" ")
                                                print(" ")
                                            else: 
                                                print("SE ESPERABA UN PUNTO Y COMA")

                                        else:
                                            print("SE ESPERABA UN CORCHETE DE CIERRE")
                                            break
                                    else:
                                        print("SE ESERABA LA CANTIDAD DE UNIDADES VENDIDAS")
                                        break
                                else: 
                                    print("SE ESPERABA UNA COMA")
                                    break
                            else:
                                print("SE ESPERABA EL PRECIO DEL PRODUCTO") 
                                break                          
                        else:
                            print("SE ESPERABA UNA COMA")
                            break
                    else:#SINO SE CUMPLE ENTONCES QUE SE ROMPA EL CICLO 
                        print("SE ESPERABAn CADENA")
                        break
                    continue
        if len(self.arreglo_productos) >0:
            return self.arreglo_productos
        else: 
            return self.arreglo_productos