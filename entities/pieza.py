class Pieza:
    def __init__(self, codigo, descripcion, costo, lote_reposicion, cantidad_disponible=0):
        self.codigo = codigo
        self.descripcion = descripcion
        self.costo = costo
        self.lote_reposicion = lote_reposicion
        self.cantidad_disponible = cantidad_disponible


    def __str__(self):
        return (f"[{self.codigo}] {self.descripcion} | "
                f"Costo: ${self.costo:.2f} | "
                f"Lote: {self.lote_reposicion} | "
                f"Stock: {self.cantidad_disponible}")
