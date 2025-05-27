from datetime import datetime

class Reposicion:
    def __init__(self, pieza, cantidad_lotes):
        self.pieza = pieza
        self.cantidad_lotes = cantidad_lotes
        self.fecha = datetime.now()
        self.costo_total = self.calcular_costo_total()

    def calcular_costo_total(self):
        return self.cantidad_lotes * self.pieza.lote_reposicion * self.pieza.costo

    def __str__(self):
        return (f"Reposición de {self.cantidad_lotes} lote(s) para '{self.pieza.descripcion}' "
                f"el {self.fecha.strftime('%Y-%m-%d %H:%M')} | Costo total: ${self.costo_total:.2f}")
