nombres = []
apellidos = []
for names in range(3):
    nombres.append(input("Ingrese un Nombre -> "))
    apellidos.append(input("Ingrese un Apellido -> "))
for i in range(len(nombres)):
    print(nombres[i] + " " + apellidos[i])