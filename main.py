#ESTE PROGRAMA ESTA DISEÑADO PARA LEER DOS ARCHIVOS Y DEVOLVER UN REPORTE CON ESPECIFICACIONES DADAS
from funciones import recuperar
from Lexico_instrucc import Lexico_instrucciones
from Analizador_sintactico import Sintactico_instrucciones
from Lexico_data import Lexico_data
from Sintactico_data import Sintactico_data
from Producto import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

def menu():
    salir = False
    contenido_instru = ''
    contenido_data =""
    contenido_instru =""
    lexico_intrucciones = None
    sintactico_intrucciones2 = []
    sintactico_intrucciones = []
    instrucciones_generales = []
    completo = True
    #DATOS DEL REPORTE COMPLETO
    nombre_archivo = ''
    tipo_grafico = ''
    titulo_graf = ''
    titulo_x = ''
    titulo_y = ''



    while salir != True:    
        print("")    
        print("1. CARGAR DATA")
        print("2. CARGAR INSTRUCCIONES")
        print("3. ANALIZAR")
        print("4. REPORTES ")
        print("5. SALIR")
        print("")
        opcion = int(input("DIGITE EL NUMERO DE LA OPCION CORRESPONDIENTE "))
        

        if(opcion == 1):
            print("AQUI SE SELECCIONA DATA ")
            contenido_data = recuperar()
            print(contenido_data)

        if(opcion == 2):
            print("AQUI SE SELECCIONA INSTRUCCIONES.LFP ")
            contenido_instru = recuperar()
            print(contenido_instru)
    
        if(opcion == 3):
            print("AQUI SE ANALIZA ")
            lexico_intrucciones = Lexico_instrucciones(contenido_instru)
            lexico_intrucciones.printTokens()
            #print("****************************************************************")
            #lexico_intrucciones.GuardarDatos() no sirve
            sintactico_intrucciones = Lexico_instrucciones.lista_tokens
            sintactico_intrucciones2 = Sintactico_instrucciones(sintactico_intrucciones)
            #sintactico_intrucciones2.printTokens() no sirve
            
            if Sintactico_instrucciones.arreglo_lleno[0] == False:
                print("INCOMPLETO")
                salir = True
            else:
                print("SATISFACTORIO")
                for m in range(6):
                    print(Sintactico_instrucciones.arreglo_lleno[m])
                print("--------------------------------------------------------------------------------")
                print("-------------------------------------------------------------------------------")
                print("")
                #ANALIZADOR SINTACTICO DE DATA 
                lexico_data = Lexico_data(contenido_data)
                lexico_data.printTokens()
                print("")
                sintactico_data = Lexico_data.lista_tokens
                Sintactico_data(sintactico_data)
                print(len(Sintactico_data.arreglo_productos))

                #VER SI DATA ESTA COMPLETO
                #SI ARREGLO DE PRODUCTOS ESTA LLENO
                if(len(Sintactico_data.arreglo_productos) == 0):
                    print("aqui se activo arreglo productos")
                    salir = True
                #SI EXISTE EL NOMBRE DEL MES Y EL AÑO 
                if len(Sintactico_data.datos_generales[0])>0 and len(Sintactico_data.datos_generales[1])>0:
                    
                    print("")
                else:
                    print("aqui fue mes y año ")
                    salir = True

                #EXTRAER DATOS PARA EL REORTE
                nombre_archivo = str(Sintactico_instrucciones.arreglo_lleno[1])+'.png'
                tipo_grafico = Sintactico_instrucciones.arreglo_lleno[2]
                
                #TITULO DEL GRAFICO
                if Sintactico_instrucciones.arreglo_lleno[3] == None:
                    print("titulo de mes y año")
                    titulo_graf = "REPORTE DE VENTAS "+Sintactico_data.datos_generales[0]+" - "+str(Sintactico_data.datos_generales[1])
                else:
                    print("SI HAY TITULO")
                    titulo_graf = Sintactico_instrucciones.arreglo_lleno[3]

                #TITULOS X Y Y
                if Sintactico_instrucciones.arreglo_lleno[4] == None:
                    print("")
                else:
                    titulo_x = Sintactico_instrucciones.arreglo_lleno[4]

                if Sintactico_instrucciones.arreglo_lleno[5] == None:
                    pass
                else:
                    titulo_y = Sintactico_instrucciones.arreglo_lleno[5]


                print("")
                print("NOMBRE ARCHIVO: "+nombre_archivo)
                print("TIPO GRAFICO: "+tipo_grafico)
                print("TITULO GRAFICO: "+str(titulo_graf))
                if len(titulo_x)>0:
                    print("TITULO X: "+titulo_x)
                if len(titulo_y)>0:
                    print("TITULO Y: "+titulo_y)

                print("")
                arreglo_x = []
                arreglo_y = []
                for producto in Sintactico_data.arreglo_productos:
                    print(producto.producto + " -> precio: " + str(producto.precio_u)+" ganancia: "+str(producto.ganancia))### aqui mi quede
                    arreglo_x.append(producto.producto)
                    arreglo_y.append(producto.ganancia)

                #GENERACION DE GRAFICA 
                
                if tipo_grafico.upper() == 'BARRAS':
                
                    plt.title(titulo_graf, 
                            fontdict={'family': 'serif', 
                                        'color' : 'darkblue',
                                        'weight': 'bold',
                                        'size': 18})
                    plt.xlabel(titulo_x, size = 16,)
                    plt.ylabel(titulo_y, size = 16)   
                    #Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
                    plt.bar(arreglo_x, arreglo_y)
                    plt.savefig(nombre_archivo)
                    #Finalmente mostramos la grafica con el metodo show()
                    plt.show()


                    
                if tipo_grafico.upper() == 'LINEAS':
                    x = np.linspace(0, 2, 10)
                    x1 = arreglo_x
                    y1 = arreglo_y
                    #Generamos una grafica lineal para una recta en X
                    plt.plot(x1, y1, marker ='o')
                    plt.title(titulo_graf, 
                            fontdict={'family': 'serif', 
                                        'color' : 'darkblue',
                                        'weight': 'bold',
                                        'size': 18})
                    plt.xlabel(titulo_x, size = 16,)
                    plt.ylabel(titulo_y, size = 16) 
                    plt.legend()
                    plt.savefig(nombre_archivo)
                    plt.show()



                if tipo_grafico.upper() == 'PIE':
                    plt.pie(arreglo_y, labels=arreglo_x, autopct="%0.1f %%")
                    plt.axis("equal")
                    plt.title(titulo_graf, 
                            fontdict={'family': 'serif', 
                                        'color' : 'darkblue',
                                        'weight': 'bold',
                                        'size': 18})
                    plt.savefig(nombre_archivo)
                    plt.show()
            

                
                
                    

        if(opcion == 4):
            print("AQUI VAN LOS REPORTES")
            #PRODUCTO MAS VENDIDO Y MENOS VENDIDO
            #for i in arreglo_ganancias:
             #   print(i)
                        
            print("")
            print("")
            arreglo_ganancias = ordenamiento(Sintactico_data.arreglo_productos)
            print("")
            print("")
            for producto in arreglo_ganancias:
                print(producto.producto + " -> precio: " + str(producto.precio_u)+" ganancia: "+str(producto.ganancia))

            menos_vendido = arreglo_ganancias[0]
            mas_vendido = arreglo_ganancias[len(arreglo_ganancias)-1]
            print("")
            print("")
            print(menos_vendido.producto + " -> precio: " + str(menos_vendido.precio_u)+" ganancia: "+str(menos_vendido.ganancia))
            print(mas_vendido.producto + " -> precio: " + str(mas_vendido.precio_u)+" ganancia: "+str(mas_vendido.ganancia))

            print("")
            reporte(arreglo_ganancias,mas_vendido,menos_vendido)

            
            

        if(opcion == 5):
            print("ADIOS!!!! :)")
            salir = True


def ordenamiento(arreglo):
    #for producto in arreglo:
     #           print(producto.producto + " -> precio: " + str(producto.precio_u)+" ganancia: "+str(producto.ganancia))### aqui mi quede

    for i in range(1,len(arreglo)):
        for j in range(0,len(arreglo)-i):
            if(arreglo[j+1].ganancia < arreglo[j].ganancia):
                aux=arreglo[j]
                arreglo[j]=arreglo[j+1]
                arreglo[j+1]=aux
    return arreglo
 
def reporte(arreglo,mas, menos):
    file = open("REPORTE.html", "w")
    file.write("<HTML>")
    file.write("<HEAD><TITLE>REPORTE</TITLE>")
    file.write("<link rel=\"stylesheet\"  href=\"estilos.css\">")
    file.write("</head>")
    file.write("<body>")
    file.write("<CENTER><H1><b>------------------------------- REPORTE -------------------------------</b></H1>")
    file.write("</CENTER>")
    file.write("<img src=\"2d.gif\" width=\"300\" height=\"200\" align=right>")
    file.write("<form action=\"\"> ")
    file.write("<p><b>&nbsp &nbsp &nbsp &nbsp &nbsp &nbspYENIFER ESTER YOC LARIOS -------->&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 201952336 </b></p>")
    file.write("<p><b>&nbsp &nbsp &nbsp &nbsp &nbsp &nbspPRODUCTO MAS VENDIDO -------->&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp "+ mas.producto+"</b></p>")
    file.write("<p><b>&nbsp &nbsp &nbsp &nbsp &nbsp &nbspPRODUCTO MENOS VENDIDO -------->&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp "+ menos.producto+"</b></p>")
    file.write("<br>")
    file.write("<div  id = \"main-container\" >")
    file.write("<b>")
    file.write("<table>")
    file.write("<thead>")
    file.write("<tr>")
    file.write("<th> NOMBRE PRODUCTO   </th><th>PRECIO</th><th>CANTIDAD</th><th>GANANCIA</th>")
    file.write("</tr>")
    file.write("</thead>")
            
    for producto in arreglo:
                file.write("<tr>")
                file.write("<td> "+producto.producto+"</td><td>"+str(producto.precio_u)+"</td><td>"+str(producto.cantidad)+"</td><td>"+str(producto.ganancia)+"</td>")
                file.write("</tr>")
			
    file.write("</b>")
    file.write("</table>")
    file.write("</div>")

    file.write("</BODY>\r\n"+ "</HTML>");			
    file.close()
    print("")
    print("SE HA CREADO EL REPORTE CON EXITO")
    print("")


def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2 
    menu()

if __name__ == "__main__":
    main()
  

    