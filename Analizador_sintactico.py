from Token import Token
from TypeToken import TypeToken

class Sintactico_instrucciosnes():

    nombre_grafico = ''
    grafica = ''
    titulo = ''
    titulox =''
    bandera_titulo = False
    tiruloy = ''
    arreglo_lleno = [False, None, None, None, None, None]

    def __init__(self,tokens):

        self.tokens= tokens
        longitud_arr = len(tokens)
        bandera_n= False #SIRVEN PARA MONITOREAR QUE AMBOS CAMPOS SE CUMPLAN
        bandera_g= False
        barras = False
        si_titulo = False

        arreglo_nombre = self.Buscar_elemento(TypeToken.NOMBRE.name)
        arreglo_grafica= self.Buscar_elemento(TypeToken.GRAFICA.name)
        arreglo_titulo = [False, None]
        arreglo_titulox = [False, None]
        arreglo_tituloy = [False, None]
        if arreglo_nombre[0] == True and arreglo_grafica[0] == True:#QUE DEVUELVA UN TRUE SI LA CONDICION SE CUMPLE 
            self.nombre_grafico = arreglo_nombre[1]
            self.grafica = arreglo_grafica[1]
            print("ESTA completo") 
            print(self.nombre_grafico)
            print(self.grafica)
            self.arreglo_lleno[0] = True
            self.arreglo_lleno[1] = self.nombre_grafico
            self.arreglo_lleno[2] = self.grafica
            #OPCIONALES ******************************************************
            arreglo_titulo = self.Buscar_elemento(TypeToken.TITULO.name)
            self.arreglo_lleno[3] = arreglo_titulo[1]
            #SI ES DE BARRAS QUE BUSQUE X Y Y 
            if self.arreglo_lleno[2].upper() == 'BARRAS' or self.arreglo_lleno[2].upper() =='LINEAS':
                arreglo_titulox = self.Buscar_elemento(TypeToken.TITULOX.name)
                self.arreglo_lleno[4] = arreglo_titulox[1]

                arreglo_tituloy = self.Buscar_elemento(TypeToken.TITULOY.name)
                self.arreglo_lleno[5] = arreglo_tituloy[1]
            else:
                print("EL NOMBRE NO ERA BARRAS")
        else:
            print("NO ESTA COMPLETO")
      
    def Ver_completo(tokens):#ESTE METODO VERIFICA QUE LOS CAMPOS OBLIGATORIOS ESTEN EN EL ARCHIVO DE ENTRADA
        longitud_arr = len(tokens)
        bandera_n= False #SIRVEN PARA MONITOREAR QUE AMBOS CAMPOS SE CUMPLAN
        bandera_g= False
        barras = False
        si_titulo = False
        for i in range(longitud_arr):# SE RECORRE LA LONGITUD DEL ARREGLO
                if tokens[i].type == TypeToken.NOMBRE.name:
                    if tokens[i+1].type == TypeToken.DOS_PUNTOS.name:#SE VERIFICA QUE CUMPLA DETEMINDAMENTE CON CAMPO Y CON CONTENIDO
                        if tokens[i+2].type == TypeToken.CADENA.name:
                            print("campo completo")
                            nombre_grafico = tokens[i+2].lexema
                            
                            bandera_n= True#SI YA SE ENCOTRO QUE NO LO SIGA BUSCANDO
                            print(nombre_grafico)
                        else:
                            print("SE ESPERABA UNA CADENA")
                            break
                    else:#SINO SE CUMPLE ENTONCES QUE SE ROMPA EL CICLO 
                        print("SE ESPERABAn DOS PUNTOS")
                        break
            
                    print("nombre si esta")
                    
                    
                    continue

                if tokens[i].type == TypeToken.GRAFICA.name:
                    if tokens[i+1].type == TypeToken.DOS_PUNTOS.name:
                        if tokens[i+2].type == TypeToken.CADENA.name:
                            print("campo completo")
                            grafica = tokens[i+2].lexema
                            print(grafica)
                            bandera_g= True
                        else:
                            print("SE ESPERABA UNA CADENA")
                            break
                    else:
                        print("SE ESPERABAn DOS PUNTOS")
                        break
                    print("grafica si esta")
                    
                    continue   
        if bandera_n == True and bandera_g == True:#QUE DEVUELVA UN TRUE SI LA CONDICION SE CUMPLE 
            print("ESTA completo") 
            return True
        else: 
            print("ESTA incompleto")  
            return False
        
    def Buscar_elemento(self, tipo):
        longitud_arr = len(self.tokens)
        salida = [False, None]
        encontre = False
        for i in range(longitud_arr):# SE RECORRE LA LONGITUD DEL ARREGLO
                if self.tokens[i].type == tipo:
                    if self.tokens[i+1].type == TypeToken.DOS_PUNTOS.name:#SE VERIFICA QUE CUMPLA DETEMINDAMENTE CON CAMPO Y CON CONTENIDO
                        if self.tokens[i+2].type == TypeToken.CADENA.name:
                            print("campo completo")
                            salida[0] = True
                            salida[1] = self.tokens[i+2].lexema
                            
                            encontre = True
                        else:
                            print("SE ESPERABA UNA CADENA")
                            break
                    else:#SINO SE CUMPLE ENTONCES QUE SE ROMPA EL CICLO 
                        print("SE ESPERABAn DOS PUNTOS")
                        break
                    continue
        if encontre == True:
            return salida
        else: 
            salida[0] = False
            salida[1] = None
            return salida

    def printTokens(self):
        
        print("ESTE ES EL ARREGLO DEL ANALIZADOR SINTACTICO")
        for token in self.arreglo_tok:
            print(token.lexema + " -> Tipo: " + str(token.type))

    