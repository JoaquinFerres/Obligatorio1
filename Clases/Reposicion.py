from datetime import datetime

class Reposicion:
    def __init__(self, pieza, cantidad_lotes):
        self.pieza = pieza
        self.cantidad_lotes = cantidad_lotes
        self.fecha = datetime.now()
        self.costo_total = cantidad_lotes * pieza.lote_reposicion * pieza.costo
