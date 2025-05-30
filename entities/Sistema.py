from pieza import Pieza
from excepcion_pieza_ya_existe import ExcepcionPiezaYaExiste
from maquina import Maquina
from requerimiento import Requerimiento
from excepcion_maquina_ya_existe import ExcepcionMaquinaYaExiste
from cliente import ClienteParticular, Empresa
from excepcion_cliente_ya_existe import ExcepcionClienteYaExiste
from pedido import Pedido
from reposicion import Reposicion





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
        return any(p.descripcion == descripcion for p in self.piezas)
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

                cantidad = 0

                codigo = self.generar_codigo_pieza()
                nueva_pieza = Pieza(codigo, descripcion, costo, lote, cantidad)
                self.piezas.append(nueva_pieza)

                print(f"\n Pieza registrada exitosamente:/n{nueva_pieza}")

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
                if any(m.descripcion == descripcion for m in self.maquinas):
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

#registrar reposicion

    def registrar_reposicion(self):
        print("\n--- Registrar reposición de pieza ---")
        if not self.piezas:
            print("  No hay piezas registradas.")
            return

        print("Piezas disponibles:")
        for p in self.piezas:
            print(f"[{p.codigo}] {p.descripcion} | Lote: {p.lote_reposicion} | Stock: {p.cantidad_disponible}")

        try:
            codigo = int(input("Ingrese el código de la pieza: "))
            pieza = None
            for p in self.piezas:
                if p.codigo == codigo:
                    pieza = p
                    break

            if not pieza:
                print("  Pieza no encontrada.")
                return

            cantidad_lotes = int(input("Cantidad de lotes a reponer: "))
            if cantidad_lotes <= 0:
                print("  La cantidad debe ser mayor a 0.")
                return

            reposicion = Reposicion(pieza, cantidad_lotes)
            self.reposiciones.append(reposicion)

            # Actualizar stock
            cantidad_agregada = cantidad_lotes * pieza.lote_reposicion
            pieza.cantidad_disponible += cantidad_agregada

            print(f"\n Reposición registrada:\n{reposicion}")
            print(f" Stock actualizado: {pieza.cantidad_disponible} unidades disponibles")

            self.completar_pedidos_pendientes()

        except ValueError:
            print("  Entrada inválida.")

        
#Completar pedidos pendientes

    def completar_pedidos_pendientes(self):
        for pedido in self.pedidos:
            if pedido.estado == "pendiente":
                maquina = pedido.maquina
                puede_entregarse = True
                for req in maquina.requerimientos:
                    if req.pieza.cantidad_disponible < req.cantidad:
                        puede_entregarse = False
                        break
    
                if puede_entregarse:
                    # Entregar y descontar stock
                    for req in maquina.requerimientos:
                        req.pieza.cantidad_disponible -= req.cantidad
                    pedido.entregar()
                    print(f" Pedido pendiente actualizado a ENTREGADO para cliente {pedido.cliente.id}")



#listar clientes
    def listar_clientes(self):
        print("\n--- Lista de clientes registrados ---")
        if not self.clientes:
            print("  No hay clientes registrados.")
            return

        for cliente in self.clientes:
            print(cliente)

#listar pedidos

    def listar_pedidos(self):
        print("\n--- Lista de pedidos ---")
        if not self.pedidos:
            print("  No hay pedidos registrados.")
            return

        print("¿Desea filtrar por estado?")
        print("1. Sí")
        print("2. No")
        opcion_filtro = input("Seleccione una opción: ").strip()

        pedidos_a_mostrar = self.pedidos

        if opcion_filtro == "1":
            print("1. Pendientes")
            print("2. Entregados")
            estado = input("Seleccione el estado: ").strip()
            if estado == "1":
                pedidos_a_mostrar = []
                for pedido in self.pedidos:
                    if pedido.estado == "pendiente":
                        pedidos_a_mostrar.append(pedido)

            elif estado == "2":
                pedidos_a_mostrar = []
                for pedido in self.pedidos:
                    if pedido.estado == "entregado":
                        pedidos_a_mostrar.append(pedido)
            else:
                print("  Opción inválida. Mostrando todos los pedidos.")

        if not pedidos_a_mostrar:
            print("  No hay pedidos con ese filtro.")
            return

        for pedido in pedidos_a_mostrar:
            print(pedido)

#listar piezas
    def listar_piezas(self):
        print("\n--- Lista de piezas ---")
        if not self.piezas:
            print("  No hay piezas registradas.")
            return

        for pieza in self.piezas:
            faltante = 0
            for pedido in self.pedidos:
                if pedido.estado == "pendiente":
                    for req in pedido.maquina.requerimientos:
                        if req.pieza.codigo == pieza.codigo:
                            faltante += req.cantidad

            faltante_real = max(0, faltante - pieza.cantidad_disponible)

            if faltante_real > 0:
                recomendado = (faltante_real + pieza.lote_reposicion - 1) // pieza.lote_reposicion
            else:
                recomendado = 0

            print(f"[{pieza.codigo}] {pieza.descripcion} | Stock: {pieza.cantidad_disponible} | "
                  f"Lote: {pieza.lote_reposicion} | Faltante: {faltante_real} | "
                  f"Reponer: {recomendado} lote(s)")


#listar maquinas

    def listar_maquinas(self):
        print("\n--- Lista de máquinas ---")
        if not self.maquinas:
            print("  No hay máquinas registradas.")
            return

        for maquina in self.maquinas:
            disponible = True
            for req in maquina.requerimientos:
                if req.pieza.cantidad_disponible < req.cantidad:
                    disponible = False
                    break

            if disponible:
                estado = "DISPONIBLE"
            else:
                estado = "NO DISPONIBLE"

            costo = maquina.calcular_costo_produccion()
            print(f"[{maquina.codigo}] {maquina.descripcion} | Costo: ${costo:.2f} | Estado: {estado}")


#listar contabilidad

    def mostrar_contabilidad(self):
        print("\n--- Contabilidad ---")

        costo_total = 0
        ingreso_total = 0

        for pedido in self.pedidos:
            if pedido.estado == "entregado":
                costo_total += pedido.maquina.calcular_costo_produccion()
                ingreso_total += pedido.precio_venta

        ganancia = ingreso_total - costo_total
        impuesto = ganancia * 0.25
        ganancia_final = ganancia - impuesto

        print(f"Costo total de producción: ${costo_total}")
        print(f"Ingreso total por ventas: ${ingreso_total}")
        print(f"Ganancia bruta: ${ganancia}")
        print(f"Impuesto (IRAE 25%): ${impuesto}")
        print(f"Ganancia neta: ${ganancia_final}")
