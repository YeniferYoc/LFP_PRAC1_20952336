class Producto():
    def __init__(self,producto, precio_u, cantidad,ganancia):
        self.producto = producto
        self.precio_u = precio_u
        self.cantidad = cantidad
        self.ganancia = ganancia

    def dar_producto(self):
        return self.producto
    
    def dar_precio_u(self):
        return self.precio_u
    
    def dar_cantidad(self):
        return self.cantidad
    
    def dar_ganancia(self):
        return self.ganancia
    
    def dar_todo(self):
        print("NOMBRE PRODUCTO: "+self.producto+" PRECIO: "+str(self.precio_u)+" CANTIDAD VENDIDA: "+str(self.cantidad)+" GANANCIA: "+str(self.ganancia))
