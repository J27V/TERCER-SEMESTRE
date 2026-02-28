diccionario = {
    "time": "tiempo",
    "person": "persona",
    "year": "año",
    "way": "camino",
    "day": "día",
    "thing": "cosa",
    "man": "hombre",
    "world": "mundo",
    "life": "vida",
    "hand": "mano",
    "part": "parte",
    "child": "niño",
    "eye": "ojo",
    "woman": "mujer",
    "place": "lugar",
    "work": "trabajo",
    "week": "semana",
    "case": "caso",
    "point": "punto",
    "government": "gobierno",
    "company": "empresa"
}


def traducir_frase():
    frase = input("\nIngrese una frase: ").lower()
    palabras = frase.split(" ")
    resultado = ""

    for palabra in palabras:
        limpia = palabra.strip(".,;!?")

        if limpia in diccionario:
            resultado += diccionario[limpia] + " "
        else:
            resultado += palabra + " "

    print("\nTraducción:")
    print(resultado)


def agregar_palabra():
    ingles = input("\nIngrese palabra en inglés: ").lower()
    espanol = input("Ingrese traducción en español: ").lower()

    if ingles not in diccionario:
        diccionario[ingles] = espanol
        print("Palabra agregada correctamente.")
    else:
        print("La palabra ya existe en el diccionario.")


def menu():
    opcion = -1

    while opcion != 0:
        print("\n==================== MENÚ ====================")
        print("1. Traducir una frase")
        print("2. Agregar palabras al diccionario")
        print("0. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except:
            print("Ingrese un número válido.")
            continue

        if opcion == 1:
            traducir_frase()
        elif opcion == 2:
            agregar_palabra()
        elif opcion == 0:
            print("Programa finalizado.")
        else:
            print("Opción inválida.")


menu()