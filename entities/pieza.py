class Pieza:
    def __init__(self, codigo, descripcion, costo, lote_reposicion, cantidad_disponible=0):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__costo = costo
        self.__lote_reposicion = lote_reposicion
        self.__cantidad_disponible = cantidad_disponible

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def costo(self):
        return self.__costo
    
    @property
    def lote_reposicion(self):
        return self.__lote_reposicion
    
    @property
    def cantidad_disponible(self):
        return self.__cantidad_disponible

    @cantidad_disponible.setter
    def cantidad_disponible(self,nueva_cantidad):
        self.__cantidad_disponible = nueva_cantidad

    def __str__(self):
        return (f"[{self.codigo}] {self.descripcion} | "
                f"Costo: ${self.costo} | "
                f"Lote: {self.lote_reposicion} | "
                f"Stock: {self.cantidad_disponible}")
