class Sistema:
    def __init__(self):
        self.piezas = []
        self.maquinas = []
        self.clientes = []
        self.pedidos = []
        self.reposiciones = []

class Pieza:
    def __init__(self, codigo, descripcion, costo, lote_reposicion, cantidad_disponible=0):
        self.codigo = codigo
        self.descripcion = descripcion
        self.costo = costo
        self.lote_reposicion = lote_reposicion
        self.cantidad_disponible = cantidad_disponible

class Maquina:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.requerimientos = []  # lista de objetos Requerimiento

    def calcular_costo_produccion(self):
        return sum(req.pieza.costo * req.cantidad for req in self.requerimientos)

class Requerimiento:
    def __init__(self, pieza, cantidad):
        self.pieza = pieza
        self.cantidad = cantidad

class Cliente:
    def __init__(self, id, telefono, email):
        self.id = id
        self.telefono = telefono
        self.email = email

class ClienteParticular(Cliente):
    def __init__(self, id, cedula, nombre, telefono, email):
        super().__init__(id, telefono, email)
        self.cedula = cedula
        self.nombre = nombre

class Empresa(Cliente):
    def __init__(self, id, rut, nombre, web, telefono, email):
        super().__init__(id, telefono, email)
        self.rut = rut
        self.nombre = nombre
        self.web = web


from datetime import datetime

class Pedido:
    def __init__(self, cliente, maquina, fecha_recepcion=None):
        self.cliente = cliente
        self.maquina = maquina
        self.fecha_recepcion = fecha_recepcion or datetime.now()
        self.fecha_entrega = None
        self.estado = "pendiente"  # o "entregado"


from datetime import datetime

class Reposicion:
    def __init__(self, pieza, cantidad_lotes):
        self.pieza = pieza
        self.cantidad_lotes = cantidad_lotes
        self.fecha = datetime.now()
        self.costo_total = cantidad_lotes * pieza.lote_reposicion * pieza.costo
