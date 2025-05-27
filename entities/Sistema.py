from pieza import Pieza
from ..Excepciones.ExcepcionPiezaYaExiste import ExcepcionPiezaYaExiste
from Maquina import Maquina
from Requerimiento import Requerimiento
from ..Excepciones.ExcepcionMaquinaYaExiste import ExcepcionMaquinaYaExiste
from Cliente import ClienteParticular, Empresa
from ..Excepciones.ExcepcionClienteYaExiste import ExcepcionClienteYaExiste
from Pedido import Pedido




class Sistema:
    def __init__(self):
        self.piezas = []
        self.maquinas = []
        self.clientes = []
        self.pedidos = []
        self.reposiciones = []
        self.piezas = []
        self.ultimo_codigo_pieza = 0

#registrar piezas

    def generar_codigo_pieza(self):
        self.ultimo_codigo_pieza += 1
        return self.ultimo_codigo_pieza

    def descripcion_pieza_existe(self, descripcion):
        return any(p.descripcion() == descripcion() for p in self.piezas)
        pass
    def registrar_pieza(self):
        print("\n--- Registrar nueva pieza ---")
        while True:
            try:
                descripcion = input("Descripción: ")
                if not descripcion:
                    raise ValueError("La descripción no puede estar vacía.")
                if self.descripcion_pieza_existe(descripcion):
                    raise ExcepcionPiezaYaExiste(f"La pieza con descripción '{descripcion}' ya existe.")

                costo = float(input("Costo unitario (USD): "))
                if costo <= 0:
                    raise ValueError("El costo debe ser mayor a 0.")

                lote = int(input("Tamaño del lote de reposición: "))
                if lote <= 0:
                    raise ValueError("El lote debe ser mayor a 0.")

                cantidad = input("Cantidad disponible [0 por defecto]: ")
                cantidad = int(cantidad) if cantidad else 0
                if cantidad < 0:
                    raise ValueError("La cantidad no puede ser negativa.")

                codigo = self.generar_codigo_pieza()
                nueva_pieza = Pieza(codigo, descripcion, costo, lote, cantidad)
                self.piezas.append(nueva_pieza)

                print(f"\n Pieza registrada exitosamente:\n{nueva_pieza}")
                break

            except ValueError as ve:
                print(f"  Error: {ve}")
            except ExcepcionPiezaYaExiste as epe:
                print(f"  Error: {epe}")

#registrar maquinas

    def registrar_maquina(self):
        print("\n--- Registrar nueva máquina ---")
        while True:
            try:
                descripcion = input("Descripción: ")
                if not descripcion:
                    raise ValueError("La descripción no puede estar vacía.")
                if any(m.descripcion() == descripcion() for m in self.maquinas):
                    raise ExcepcionMaquinaYaExiste(f"La máquina con descripción '{descripcion}' ya existe.")

                codigo = len(self.maquinas) + 1
                maquina = Maquina(codigo, descripcion)

                piezas_disponibles = self.piezas.copy()
                if not piezas_disponibles:
                    print("  No hay piezas registradas para asociar a la máquina.")
                    return

                while True:
                    agregar = input("¿Agregar requisito de pieza? (Sí/No): ")
                    if agregar == "no":
                        break
                    elif agregar == "sí" or agregar == "si":
                        # Mostrar piezas disponibles
                        print("\nPiezas disponibles:")
                        for p in piezas_disponibles:
                            print(p)

                        try:
                            cod_pieza = int(input("Ingrese el código de la pieza: "))
                            pieza = next((p for p in piezas_disponibles if p.codigo == cod_pieza), None)
                            if not pieza:
                                print("  Código de pieza inválido.")
                                continue

                            cantidad = int(input("Cantidad necesaria: "))
                            if cantidad <= 0:
                                print("  La cantidad debe ser mayor que 0.")
                                continue

                            requerimiento = Requerimiento(pieza, cantidad)
                            maquina.agregar_requerimiento(requerimiento)

                            # Eliminar pieza seleccionada de la lista para evitar duplicados
                            piezas_disponibles.remove(pieza)

                        except ValueError:
                            print("  Entrada inválida.")
                    else:
                        print("  Debe responder 'Sí' o 'No'.")

                if not maquina.requerimientos:
                    print("  La máquina debe tener al menos una pieza.")
                    return

                self.maquinas.append(maquina)
                print(f"\n Máquina registrada exitosamente:\n{maquina}")
                break

            except ValueError as ve:
                print(f"  Error: {ve}")
            except ExcepcionMaquinaYaExiste as eme:
                print(f"  Error: {eme}")


#registrar clientes

    def registrar_cliente(self):
        print("\n--- Registrar nuevo cliente ---")
        while True:
            try:
                tipo = input("Tipo de cliente (1: Particular, 2: Empresa): ")
                if tipo not in ("1", "2"):
                    raise ValueError("Opción inválida. Debe ser 1 o 2.")

                id_cliente = len(self.clientes) + 1

                if tipo == "1":
                    cedula = input("Cédula: ")
                    if not cedula:
                        raise ValueError("La cédula no puede estar vacía.")
                    if any(isinstance(c, ClienteParticular) and c.cedula == cedula for c in self.clientes):
                        raise ExcepcionClienteYaExiste("Ya existe un cliente con esa cédula.")

                    nombre = input("Nombre completo: ")
                    telefono = input("Teléfono: ")
                    email = input("Correo electrónico: ")

                    cliente = ClienteParticular(id_cliente, cedula, nombre, telefono, email)

                else:
                    rut = input("RUT: ")
                    if not rut:
                        raise ValueError("El RUT no puede estar vacío.")
                    if any(isinstance(c, Empresa) and c.rut == rut for c in self.clientes):
                        raise ExcepcionClienteYaExiste("Ya existe una empresa con ese RUT.")

                    nombre = input("Nombre: ")
                    web = input("Página web: ")
                    telefono = input("Teléfono: ")
                    email = input("Correo electrónico: ")

                    cliente = Empresa(id_cliente, rut, nombre, web, telefono, email)

                self.clientes.append(cliente)
                print(f"\n Cliente registrado exitosamente:\n{cliente}")
                break

            except ValueError as ve:
                print(f"  Error: {ve}")
            except ExcepcionClienteYaExiste as ece:
                print(f"  Error: {ece}")

#registrar pedidos

    def registrar_pedido(self):
        print("\n--- Registrar nuevo pedido ---")
        if not self.clientes:
            print("  No hay clientes registrados.")
            return
        if not self.maquinas:
            print("  No hay máquinas registradas.")
            return

        # Mostrar clientes
        print("\nClientes:")
        for c in self.clientes:
            print(c)

        try:
            id_cliente = int(input("Ingrese el ID del cliente: "))
            cliente = next((c for c in self.clientes if c.id == id_cliente), None)
            if not cliente:
                print("  Cliente no encontrado.")
                return
        except ValueError:
            print("  ID inválido.")
            return

        # Mostrar máquinas
        print("\nMáquinas disponibles:")
        for m in self.maquinas:
            print(m)

        try:
            cod_maquina = int(input("Ingrese el código de la máquina: "))
            maquina = next((m for m in self.maquinas if m.codigo == cod_maquina), None)
            if not maquina:
                print("  Máquina no encontrada.")
                return
        except ValueError:
            print("  Código inválido.")
            return

        # Verificar stock
        puede_entregarse = True
        for req in maquina.requerimientos:
            if req.pieza.cantidad_disponible < req.cantidad:
                puede_entregarse = False
                break

        pedido = Pedido(cliente, maquina)
        if puede_entregarse:
            pedido.entregar()
            # Descontar stock
            for req in maquina.requerimientos:
                req.pieza.cantidad_disponible -= req.cantidad
            print(" Pedido entregado inmediatamente.")
        else:
            print("  Pedido registrado como pendiente (no hay stock suficiente).")

        self.pedidos.append(pedido)
        print(f"Precio de venta: ${pedido.precio_venta:.2f}")

