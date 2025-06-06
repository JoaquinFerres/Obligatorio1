class Cliente:
    def __init__(self, id, telefono, email):
        self.__id = id
        self.__telefono = telefono
        self.__email = email

    @property
    def id(self):
        return self.__id
    @property
    def telefono(self):
        return self.__telefono
    @property
    def email(self):
        return self.__email
    def __str__(self):
        return f"[{self.id}] {self.email} | Tel: {self.telefono}"


class ClienteParticular(Cliente):
    def __init__(self, id, cedula, nombre_completo, telefono, email):
        super().__init__(id, telefono, email)
        self.__cedula = cedula
        self.__nombre_completo = nombre_completo
    @property
    def cedula(self):
        return self.__cedula
    @property
    def nombre_completo(self):
        return self.__nombre_completo

    def __str__(self):
        return (f"[{self.id}] PARTICULAR - {self.nombre_completo} | Cédula: {self.cedula} | "
                f"Tel: {self.telefono} | Email: {self.email}")


class Empresa(Cliente):
    def __init__(self, id, rut, nombre, web, telefono, email):
        super().__init__(id, telefono, email)
        self.__rut = rut
        self.__nombre = nombre
        self.__web = web

    @property
    def rut(self):
        return self.__rut
    @property
    def nombre(self):
        return self.__nombre
    @property
    def web(self):
        return self.__web

    def __str__(self):
        return (f"[{self.id}] EMPRESA - {self.nombre} | RUT: {self.rut} | Web: {self.web} | "
                f"Tel: {self.telefono} | Email: {self.email}")
