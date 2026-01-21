# ---------------------------------------------
# Verificación de paréntesis balanceados
# Uso de pilas (stack) en Python
# ---------------------------------------------

def esta_balanceado(expresion):
    """
    Verifica si los paréntesis, llaves y corchetes
    están correctamente balanceados en una expresión.
    """
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in expresion:
        if caracter in "({[":
            pila.append(caracter)

        elif caracter in ")}]":
            if not pila:
                return False

            tope = pila.pop()
            if pares[caracter] != tope:
                return False

    return len(pila) == 0


# ------------------ PROGRAMA PRINCIPAL ------------------
print("Programa de verificación de paréntesis balanceados")

expresion = "{7 + (8 * 5) - [(9 - 7) + (4 + 1)]}"

resultado = esta_balanceado(expresion)

if resultado:
    print("Expresión:", expresion)
    print("Resultado: Fórmula balanceada.")
else:
    print("Expresión:", expresion)
    print("Resultado: Fórmula NO balanceada.")




# ---------------------------------------------
# Resolución del problema de las Torres de Hanoi
# usando pilas (stack) en Python
# ---------------------------------------------

def hanoi(n, origen, auxiliar, destino, nombre_origen, nombre_aux, nombre_destino):
    """
    Resuelve el problema de las Torres de Hanoi usando pilas.
    """
    if n > 0:
        # Mover n-1 discos al auxiliar
        hanoi(n - 1, origen, destino, auxiliar,
              nombre_origen, nombre_destino, nombre_aux)

        # Mover el disco principal
        disco = origen.pop()
        destino.append(disco)
        print(f"Mover disco {disco} de {nombre_origen} a {nombre_destino}")

        # Mover los discos del auxiliar al destino
        hanoi(n - 1, auxiliar, origen, destino,
              nombre_aux, nombre_origen, nombre_destino)


# ------------------ PROGRAMA PRINCIPAL ------------------
if __name__ == "__main__":
    numero_discos = 3

    torre_origen = []
    torre_auxiliar = []
    torre_destino = []

    # Inicializar la torre origen
    for i in range(numero_discos, 0, -1):
        torre_origen.append(i)

    print("Pasos para resolver las Torres de Hanoi:\n")

    hanoi(numero_discos,
          torre_origen,
          torre_auxiliar,
          torre_destino,
          "Origen",
          "Auxiliar",
          "Destino")
