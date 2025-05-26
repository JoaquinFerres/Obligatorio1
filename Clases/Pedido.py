from datetime import datetime

class Pedido:
    def __init__(self, cliente, maquina, fecha_recepcion=None):
        self.cliente = cliente
        self.maquina = maquina
        self.fecha_recepcion = fecha_recepcion or datetime.now()
        self.fecha_entrega = None
        self.estado = "pendiente"  # o "entregado"