from datetime import datetime
from cliente import Empresa

class Pedido:
    def __init__(self, cliente, maquina):
        self.cliente = cliente
        self.maquina = maquina
        self.fecha_recepcion = datetime.now()
        self.fecha_entrega = None
        self.estado = "pendiente"
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        costo = self.maquina.calcular_costo_produccion()
        precio_base = costo * 1.5
        if isinstance(self.cliente, Empresa):  
            return precio_base * 0.8
        return precio_base

    def entregar(self):
        self.estado = "entregado"
        self.fecha_entrega = datetime.now()

    def __str__(self):
        estado_info = f"{self.estado.upper()} - Fecha recepción: {self.fecha_recepcion.strftime('%Y-%m-%d %H:%M')}"
        if self.estado == "entregado":
            estado_info += f" | Fecha entrega: {self.fecha_entrega.strftime('%Y-%m-%d %H:%M')}"
        return f"Pedido de máquina '{self.maquina.descripcion}' por cliente {self.cliente.id} | {estado_info}"
