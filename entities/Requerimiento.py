class Requerimiento:
    def __init__(self, pieza, cantidad):
        self.__pieza = pieza
        self.__cantidad = cantidad
    
    @property
    def pieza(self):
        return self.__pieza
    @property
    def cantidad(self):
        return self.__cantidad
