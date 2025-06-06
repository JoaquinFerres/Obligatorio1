from datetime import datetime
from cliente import Empresa

class Pedido:
    def __init__(self, cliente, maquina):
        self.__cliente = cliente
        self.__maquina = maquina
        self.__fecha_recepcion = datetime.now()
        self.__fecha_entrega = None
        self.__estado = "pendiente"
        self.precio_venta = self.calcular_precio_venta()

    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def maquina(self):
        return self.__maquina
    
    @property
    def fecha_recepcion(self):
        return self.__fecha_recepcion
    
    @property
    def fecha_entrega(self):
        return self.__fecha_entrega
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self,nuevo_estado):
        self.__estado=  nuevo_estado

    @fecha_entrega.setter
    def fecha_entrega(self, fecha):
        self.__fecha_entrega = fecha

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
