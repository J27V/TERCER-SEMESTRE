# Definición de la clase Estudiante
class Estudiante:
    def __init__(self, id_estudiante, nombres, apellidos, direccion, telefonos):
        self.id = id_estudiante
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefonos = telefonos  # Lista (array) de teléfonos

    # Método para mostrar los datos del estudiante
    def mostrar_datos(self):
        print("=== REGISTRO DE ESTUDIANTE ===")
        print(f"ID: {self.id}")
        print(f"Nombres: {self.nombres}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Direccion: {self.direccion}")
        print("Telefonos:")
        for telefono in self.telefonos:
            print(f"- {telefono}")


# Programa principal
if __name__ == "__main__":
    # Array (lista) de teléfonos
    telefonos_estudiante = [
        "0991234567",
        "0987654321",
        "0971112233"
    ]

    # Creación del objeto Estudiante
    estudiante = Estudiante(
        id_estudiante=1,
        nombres="Juan Carlos",
        apellidos="Perez Gomez",
        direccion="Av. Principal 123",
        telefonos=telefonos_estudiante
    )

    # Mostrar datos en consola
    estudiante.mostrar_datos()
