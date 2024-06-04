nombres = []
for name in range(3):
    nombres.append(input("Ingrese un nombre -> "))
nombre_mayor = nombres[0]
for names in nombres:
    if len(names) > len(nombre_mayor):
        nombre_mayor = names
print(f"El nombre con mayor caracteres es: {nombre_mayor}")