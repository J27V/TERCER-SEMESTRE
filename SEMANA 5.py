# =========================================
# EJERCICIOS DE LISTAS Y TUPLAS - POO
# =========================================

class Curso:
    def __init__(self):
        self.asignaturas = [
            "Matemáticas",
            "Física",
            "Química",
            "Historia",
            "Lengua"
        ]
        self.notas = {}

    # EJERCICIO 1
    def mostrar_asignaturas(self):
        print("\nEJERCICIO 1: Asignaturas del curso")
        for asignatura in self.asignaturas:
            print(asignatura)

    # EJERCICIO 2
    def mostrar_estudio(self):
        print("\nEJERCICIO 2: Mensaje de estudio")
        for asignatura in self.asignaturas:
            print(f"Yo estudio {asignatura}")

    # EJERCICIO 3 (CORREGIDO)
    def ingresar_y_mostrar_notas(self):
        print("\nEJERCICIO 3: Ingreso de notas")
        for asignatura in self.asignaturas:
            while True:
                try:
                    nota = float(input(f"Ingrese la nota de {asignatura}: 8"))
                    self.notas[asignatura] = nota
                    break
                except ValueError:
                    print("Error: Ingrese un número válido (use punto decimal).")

        print("\nNotas ingresadas:")
        for asignatura, nota in self.notas.items():
            print(f"En {asignatura} has sacado {nota}")


class Numeros:
    def __init__(self):
        self.lista = list(range(1, 11))

    # EJERCICIO 5
    def mostrar_inverso(self):
        print("\nEJERCICIO 5: Números del 1 al 10 en orden inverso")
        inverso = self.lista[::-1]
        print(", ".join(map(str, inverso)))


class Palindromo:
    def __init__(self):
        self.palabra = ""

    # EJERCICIO 8
    def verificar(self):
        print("\nEJERCICIO 8: Verificar palíndromo")
        self.palabra = input("Ingrese una palabra: ").lower()

        if self.palabra == self.palabra[::-1]:
            print("La palabra es un palíndromo")
        else:
            print("La palabra no es un palíndromo")


# =========================================
# PROGRAMA PRINCIPAL (ORDEN DE EJECUCIÓN)
# =========================================

def main():
    curso = Curso()
    curso.mostrar_asignaturas()
    curso.mostrar_estudio()
    curso.ingresar_y_mostrar_notas()

    numeros = Numeros()
    numeros.mostrar_inverso()

    palindromo = Palindromo()
    palindromo.verificar()


# Punto de entrada seguro
if __name__ == "__main__":
    main()
