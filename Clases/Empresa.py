from Clases.Cliente import Cliente

class Empresa(Cliente):
    def __init__(self, id, rut, nombre, web, telefono, email):
        super().__init__(id, telefono, email)
        self.rut = rut
        self.nombre = nombre
        self.web = web