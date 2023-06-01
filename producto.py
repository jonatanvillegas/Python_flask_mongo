#creando la clase producto 

class Producto:
    def __init__(self, name, description, price):
        self.name = name,
        self.description = description,
        self.preci = price
        
    #esquema de la entidad 
    def EsquemaTablaProducto(self):
        return{
            'name' : self.name,
            'description' : self.description,
            'preci' : self.price
        }