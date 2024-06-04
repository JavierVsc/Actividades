nombres = []
salir = ""
while salir != "no":
    nombres.append(input("Ingrese un Nombre -> "))
    nombre_menor = nombres[0]
    for name in nombres:
        if len(nombres) < len(nombre_menor):
            nombre_menor = name
    salir = input("¿Desea agregar otro nombre?\n").lower()
nombres.remove(nombre_menor)
print(nombres)