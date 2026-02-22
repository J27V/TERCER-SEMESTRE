# Conjunto universal: 500 ciudadanos
ciudadanos = set()

for i in range(1, 501):
    ciudadanos.add(f"Ciudadano {i}")

# Conjunto Pfizer (75 ciudadanos)
pfizer = set()
for i in range(1, 76):
    pfizer.add(f"Ciudadano {i}")

# Conjunto AstraZeneca (75 ciudadanos)
astrazeneca = set()
for i in range(50, 125):
    astrazeneca.add(f"Ciudadano {i}")

# Operaciones de teoría de conjuntos

# Unión (vacunados)
vacunados = pfizer.union(astrazeneca)

# Intersección (ambas dosis)
ambas_dosis = pfizer.intersection(astrazeneca)

# Solo Pfizer
solo_pfizer = pfizer.difference(astrazeneca)

# Solo AstraZeneca
solo_astrazeneca = astrazeneca.difference(pfizer)

# No vacunados
no_vacunados = ciudadanos.difference(vacunados)

# Mostrar resultados
def mostrar_lista(titulo, conjunto):
    print("\n" + titulo)
    for c in sorted(conjunto):
        print(c)
    print("Total:", len(conjunto))


mostrar_lista("CIUDADANOS NO VACUNADOS:", no_vacunados)
mostrar_lista("CIUDADANOS CON AMBAS DOSIS:", ambas_dosis)
mostrar_lista("CIUDADANOS SOLO PFIZER:", solo_pfizer)
mostrar_lista("CIUDADANOS SOLO ASTRAZENECA:", solo_astrazeneca)