class Condicionales:
    def mostrar_menu(self):
        print("Bienvenido al menú:")
        print("1. Personas")
        print("2. Vehiculos")
        print("3. Universidades")
        print("4. Notas")
        print("5. Salir")

    def opcion_personas(self):
        print("Hola, has presionado la opción Personas.")

    def opcion_vehiculos(self):
        print("Hola, has presionado la opción Vehiculos.")

    def opcion_universidades(self):
        print("Hola, has presionado la opción Universidades.")

    def opcion_notas(self):
        print("Hola, has presionado la opción Notas.")

    def salir(self):
        print("Saliendo del programa...")

    def procesar_opcion(self, opcion):
        opciones = {
            "1": self.opcion_personas,
            "2": self.opcion_vehiculos,
            "3": self.opcion_universidades,
            "4": self.opcion_notas,
            "5": self.salir
        }
        accion = opciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1-5).")

    def solicitar_opcion(self):
        while True:
            opcion = input("Seleccione una opción (1-5): ")
            if opcion in ['1', '2', '3', '4', '5']:
                return opcion
            else:
                print("Opción no válida. Por favor, seleccione una opción válida (1-5).")

    def main(self):
        opcion = ""
        while opcion != "5":
            self.mostrar_menu()
            opcion = self.solicitar_opcion()
            self.procesar_opcion(opcion)

if __name__ == "__main__":
    programa = Condicionales()
    programa.main()
