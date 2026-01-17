class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def contar_elementos(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador


# -------- PROGRAMA PRINCIPAL --------
if __name__ == "__main__":
    lista = ListaEnlazada()

    lista.agregar(10)
    lista.agregar(20)
    lista.agregar(30)

    print("Número de elementos en la lista:")
    print(lista.contar_elementos())
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Agregar al final
    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # EJERCICIO 2.2: Invertir la lista
    def invertir(self):
        anterior = None
        actual = self.cabeza

        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente

        self.cabeza = anterior

    # Mostrar lista
    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")


# -------- PROGRAMA PRINCIPAL --------
if __name__ == "__main__":
    lista = ListaEnlazada()

    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    lista.agregar(4)

    print("Lista original:")
    lista.mostrar()

    lista.invertir()

    print("Lista invertida:")
    lista.mostrar()
