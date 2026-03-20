class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierdo = self.insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self.insertar(nodo.derecho, valor)

        return nodo

    def buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True

        if valor < nodo.valor:
            return self.buscar(nodo.izquierdo, valor)
        else:
            return self.buscar(nodo.derecho, valor)

    def minimo(self, nodo):
        while nodo and nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo

    def maximo(self, nodo):
        while nodo and nodo.derecho:
            nodo = nodo.derecho
        return nodo

    def eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierdo = self.eliminar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self.eliminar(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

            temp = self.minimo(nodo.derecho)
            nodo.valor = temp.valor
            nodo.derecho = self.eliminar(nodo.derecho, temp.valor)

        return nodo

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecho)

    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izquierdo)
            self.preorden(nodo.derecho)

    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izquierdo)
            self.postorden(nodo.derecho)
            print(nodo.valor, end=" ")

    def altura(self, nodo):
        if nodo is None:
            return 0
        return max(self.altura(nodo.izquierdo), self.altura(nodo.derecho)) + 1

    def limpiar(self):
        self.raiz = None


# ========================
# PROGRAMA PRINCIPAL
# ========================

arbol = ArbolBST()

# 🔥 Valores precargados
valores = [10, 5, 20, 3, 7, 15, 30]

for v in valores:
    arbol.raiz = arbol.insertar(arbol.raiz, v)

print("Valores insertados automáticamente:", valores)

# Mostrar recorridos
print("\nInorden:")
arbol.inorden(arbol.raiz)

print("\nPreorden:")
arbol.preorden(arbol.raiz)

print("\nPostorden:")
arbol.postorden(arbol.raiz)

# Buscar
buscar_valor = 7
print(f"\n\nBuscar {buscar_valor}:",
      "Encontrado" if arbol.buscar(arbol.raiz, buscar_valor) else "No encontrado")

# Minimo y maximo
print("Minimo:", arbol.minimo(arbol.raiz).valor)
print("Maximo:", arbol.maximo(arbol.raiz).valor)

# Altura
print("Altura del árbol:", arbol.altura(arbol.raiz))

# Eliminar un valor
eliminar_valor = 5
arbol.raiz = arbol.eliminar(arbol.raiz, eliminar_valor)
print(f"\nDespués de eliminar {eliminar_valor} (Inorden):")
arbol.inorden(arbol.raiz)

# Limpiar árbol
arbol.limpiar()
print("\n\nÁrbol limpiado:", "Vacío" if arbol.raiz is None else "No vacío")