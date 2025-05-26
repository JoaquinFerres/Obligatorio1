class Maquina:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.requerimientos = []  # lista de objetos Requerimiento

    def calcular_costo_produccion(self):
        return sum(req.pieza.costo * req.cantidad for req in self.requerimientos)