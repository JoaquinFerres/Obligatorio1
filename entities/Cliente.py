class Cliente:
    def __init__(self, id, telefono, email):
        self.id = id
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"[{self.id}] {self.email} | Tel: {self.telefono}"


class ClienteParticular(Cliente):
    def __init__(self, id, cedula, nombre_completo, telefono, email):
        super().__init__(id, telefono, email)
        self.cedula = cedula
        self.nombre_completo = nombre_completo

    def __str__(self):
        return (f"[{self.id}] PARTICULAR - {self.nombre_completo} | Cédula: {self.cedula} | "
                f"Tel: {self.telefono} | Email: {self.email}")


class Empresa(Cliente):
    def __init__(self, id, rut, nombre, web, telefono, email):
        super().__init__(id, telefono, email)
        self.rut = rut
        self.nombre = nombre
        self.web = web

    def __str__(self):
        return (f"[{self.id}] EMPRESA - {self.nombre} | RUT: {self.rut} | Web: {self.web} | "
                f"Tel: {self.telefono} | Email: {self.email}")
