import csv      # Para trabajar con archivos .csv (guardar y leer empleados)
import os       # Para verificar si el archivo existe
import hashlib  # Para encriptar contraseñas (SHA-256)


# ========================================================
# 🔹 Clase Empleado
# ========================================================
class Empleado:
    def __init__(self, nombre, salario, contraseña_hash):
        """
        Constructor de la clase Empleado.
        Cada empleado tiene:
        - nombre (string)
        - salario (float)
        - contraseña_hash (string, la contraseña encriptada con SHA-256)
        """
        self.nombre = nombre
        self._salario = salario                  # Atributo protegido (solo dentro de la clase y subclases)
        self.__contraseña_hash = contraseña_hash # Atributo privado (solo dentro de esta clase)

    def mostrar_info(self):
        """
        Devuelve la información básica del empleado.
        """
        return f"👤 {self.nombre} | 💰 Salario: {self._salario}"

    def __verificar_contraseña(self, clave):
        """
        Método privado: verifica si la contraseña ingresada coincide
        con la contraseña encriptada almacenada.
        """
        # Encriptamos la clave ingresada con SHA-256
        clave_hash = hashlib.sha256(clave.encode()).hexdigest()
        # Comparamos con la contraseña guardada
        return clave_hash == self.__contraseña_hash

    def actualizar_salario(self, nuevo_salario, clave):
        """
        Permite actualizar el salario del empleado.
        - Primero pide la contraseña
        - Si la contraseña es correcta, actualiza el salario
        """
        if self.__verificar_contraseña(clave):
            self._salario = nuevo_salario
            return f"✅ Salario actualizado a {self._salario}"
        else:
            return "❌ Contraseña incorrecta."

    def cambiar_contraseña(self, clave_actual, nueva_clave):
        """
        Permite cambiar la contraseña.
        - Primero pide la contraseña actual
        - Si es correcta, guarda la nueva contraseña encriptada
        """
        if self.__verificar_contraseña(clave_actual):
            self.__contraseña_hash = hashlib.sha256(nueva_clave.encode()).hexdigest()
            return "🔑 Contraseña actualizada con éxito."
        else:
            return "❌ Contraseña incorrecta."

    def to_dict(self):
        """
        Convierte el objeto empleado a un diccionario.
        Esto sirve para guardar la info en un archivo CSV.
        """
        return {"nombre": self.nombre, "salario": self._salario, "contraseña": self.__contraseña_hash}


# ========================================================
# 🔹 Clase SistemaRRHH (encapsula todo el sistema)
# ========================================================
class SistemaRRHH:
    ARCHIVO = "empleados.csv"  # Nombre del archivo donde se guardan los empleados

    def __init__(self):
        # Al iniciar, cargamos los empleados desde el archivo CSV
        self.empleados = self.cargar_empleados()
        print(f"📂 {len(self.empleados)} empleados cargados desde {self.ARCHIVO}.")

    def cargar_empleados(self):
        """
        Carga los empleados desde el archivo CSV.
        Si no existe, devuelve una lista vacía.
        """
        empleados = []
        if os.path.exists(self.ARCHIVO):
            with open(self.ARCHIVO, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    empleados.append(Empleado(
                        row["nombre"],
                        float(row["salario"]),
                        row["contraseña"]
                    ))
        return empleados

    def guardar_empleados(self):
        """
        Guarda la lista de empleados en el archivo CSV.
        """
        with open(self.ARCHIVO, "w", newline="", encoding="utf-8") as f:
            campos = ["nombre", "salario", "contraseña"]
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for emp in self.empleados:
                writer.writerow(emp.to_dict())

    def buscar_empleado(self, nombre):
        """
        Busca un empleado por su nombre (no sensible a mayúsculas/minúsculas).
        """
        for emp in self.empleados:
            if emp.nombre.lower() == nombre.lower():
                return emp
        return None

    def agregar_empleado(self):
        """
        Agrega un nuevo empleado al sistema.
        Pide nombre, salario y contraseña.
        """
        nombre = input("Nombre: ").strip()

        # Validar que el salario sea un número
        while True:
            try:
                salario = float(input("Salario inicial: "))
                break
            except ValueError:
                print("⚠ Error: Ingrese un número válido para el salario.")

        # Pedir contraseña y encriptarla
        clave = input("Defina contraseña: ")
        clave_hash = hashlib.sha256(clave.encode()).hexdigest()

        # Crear el empleado y agregarlo a la lista
        self.empleados.append(Empleado(nombre, salario, clave_hash))
        print(f"✅ Empleado {nombre} agregado.")

    def listar_empleados(self):
        """
        Muestra todos los empleados registrados.
        """
        if self.empleados:
            print("\n📋 Lista de empleados:")
            for emp in self.empleados:
                print(emp.mostrar_info())
        else:
            print("⚠ No hay empleados registrados.")

    def actualizar_salario(self):
        """
        Actualiza el salario de un empleado existente.
        """
        nombre = input("Ingrese nombre del empleado: ")
        emp = self.buscar_empleado(nombre)

        if not emp:
            print("❌ Empleado no encontrado.")
            return

        clave = input("Ingrese contraseña: ")

        try:
            nuevo_salario = float(input("Ingrese nuevo salario: "))
            print(emp.actualizar_salario(nuevo_salario, clave))
        except ValueError:
            print("⚠ Error: El salario debe ser un número.")

    def cambiar_contraseña(self):
        """
        Permite cambiar la contraseña de un empleado.
        """
        nombre = input("Ingrese nombre del empleado: ")
        emp = self.buscar_empleado(nombre)

        if not emp:
            print("❌ Empleado no encontrado.")
            return

        clave_actual = input("Contraseña actual: ")
        nueva_clave = input("Nueva contraseña: ")
        print(emp.cambiar_contraseña(clave_actual, nueva_clave))

    def eliminar_empleado(self):
        """
        Elimina un empleado del sistema.
        """
        nombre = input("Ingrese nombre del empleado a eliminar: ")
        emp = self.buscar_empleado(nombre)

        if emp:
            self.empleados.remove(emp)
            print(f"🗑 Empleado {nombre} eliminado.")
        else:
            print("❌ Empleado no encontrado.")

    def menu(self):
        """
        Menú interactivo del sistema.
        """
        while True:
            print("\n=== SISTEMA RRHH ===")
            print("1. Agregar empleado")
            print("2. Listar empleados")
            print("3. Actualizar salario")
            print("4. Cambiar contraseña")
            print("5. Eliminar empleado")
            print("6. Guardar y Salir")

            opcion = input("Seleccione una opción (1-6): ")

            if opcion == "1":
                self.agregar_empleado()
            elif opcion == "2":
                self.listar_empleados()
            elif opcion == "3":
                self.actualizar_salario()
            elif opcion == "4":
                self.cambiar_contraseña()
            elif opcion == "5":
                self.eliminar_empleado()
            elif opcion == "6":
                self.guardar_empleados()
                print("💾 Datos guardados en empleados.csv")
                print("👋 Saliendo del sistema...")
                break
            else:
                print("⚠ Opción inválida.")


# ========================================================
# 🔹 EJECUCIÓN DEL PROGRAMA
# ========================================================
if __name__ == "__main__":
    sistema = SistemaRRHH()
    sistema.menu()
