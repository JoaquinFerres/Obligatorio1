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