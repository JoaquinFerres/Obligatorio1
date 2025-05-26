from Clases.Pieza import Pieza
from Excepciones.ExcepcionPiezaYaExiste import ExcepcionPiezaYaExiste

class Sistema:
    def __init__(self):
        self.piezas = []
        self.maquinas = []
        self.clientes = []
        self.pedidos = []
        self.reposiciones = []
        self.piezas = []
        self.ultimo_codigo_pieza = 0
    
    def generar_codigo_pieza(self):
        self.ultimo_codigo_pieza += 1
        return self.ultimo_codigo_pieza

    def descripcion_pieza_existe(self, descripcion):
        return any(p.descripcion.lower() == descripcion.lower() for p in self.piezas)

    def registrar_pieza(self):
        print("\n--- Registrar nueva pieza ---")
        while True:
            try:
                descripcion = input("Descripción: ").strip()
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

                cantidad = input("Cantidad disponible [0 por defecto]: ").strip()
                cantidad = int(cantidad) if cantidad else 0
                if cantidad < 0:
                    raise ValueError("La cantidad no puede ser negativa.")

                codigo = self.generar_codigo_pieza()
                nueva_pieza = Pieza(codigo, descripcion, costo, lote, cantidad)
                self.piezas.append(nueva_pieza)

                print(f"\n✅ Pieza registrada exitosamente:\n{nueva_pieza}")
                break

            except ValueError as ve:
                print(f"  Error: {ve}")
            except ExcepcionPiezaYaExiste as epe:
                print(f"  Error: {epe}")
