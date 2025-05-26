from Clases.cliente import Cliente

class ClienteParticular(Cliente):
    def __init__(self, id, cedula, nombre, telefono, email):
        super().__init__(id, telefono, email)
        self.cedula = cedula
        self.nombre = nombre