from entities.Sistema import Sistema

def mostrar_menu_principal():
    print("\n--MENÚ PRINCIPAL--")
    print("1. Registrar")
    print("2. Listar")
    print("3. Salir del Sistema")

def mostrar_menu_registrar():
    print("\n-MENÚ REGISTRAR-")
    print("1. Pieza")
    print("2. Máquina")
    print("3. Cliente")
    print("4. Pedido")
    print("5. Reposición")
    print("6. Salir")

def mostrar_menu_listar():
    print("\n-MENÚ LISTAR-")
    print("1. Clientes")
    print("2. Pedidos")
    print("3. Máquinas")
    print("4. Piezas")
    print("5. Contabilidad")
    print("6. Salir")

def main():
    sistema = Sistema()
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                mostrar_menu_registrar()
                subopcion = input("Seleccione una opción: ")

                if subopcion == "1":
                    sistema.registrar_pieza()
                elif subopcion == "2":
                    sistema.registrar_maquina()
                elif subopcion == "3":
                    sistema.registrar_cliente()
                elif subopcion == "4":
                    sistema.registrar_pedido()
                elif subopcion == "5":
                    sistema.registrar_reposicion()
                elif subopcion == "6":
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")

        elif opcion == "2":
            while True:
                mostrar_menu_listar()
                subopcion = input("Seleccione una opción: ")

                if subopcion == "1":
                    sistema.listar_clientes()
                elif subopcion == "2":
                    sistema.listar_pedidos()
                elif subopcion == "3":
                    sistema.listar_maquinas()
                elif subopcion == "4":
                    sistema.listar_piezas()
                elif subopcion == "5":
                    sistema.mostrar_contabilidad()
                elif subopcion == "6":
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")

        elif opcion == "3":
            print("¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
