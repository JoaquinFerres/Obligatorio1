class Maquina:
    def __init__(self, codigo, descripcion):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__requerimientos = []  # lista de objetos Requerimiento

    @property
    def codigo(self):
        return self.__codigo
    @property
    def descripcion(self):
        return self.__descripcion
    @property
    def requerimientos(self):
        return self.__requerimientos

    def calcular_costo_produccion(self):
        return sum(req.pieza.costo * req.cantidad for req in self.requerimientos)
    

    def agregar_requerimiento(self, requerimiento):
        self.requerimientos.append(requerimiento)


    def __str__(self):
        piezas = ", ".join(f"{r.pieza.descripcion} x{r.cantidad}" for r in self.requerimientos)
        return (f"[{self.codigo}] {self.descripcion} | Costo producción: ${self.calcular_costo_produccion():.2f} | "
                f"Piezas: {piezas}")
