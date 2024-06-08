import csv
import json

empresas_dict = {
    "empresas":[]
}

with open('Data.csv', 'r', newline = '') as csv_file:
    reader = csv.reader(csv_file)
    for count, row in enumerate(reader):
        print(count, row) #ROW = FILA
        if count == 0:
            row.append("ClasificacionEmpresa")
        else:
            venta = float(row[2])
            if venta < 100000000:
                row.append("Pequeña Empresa")
            elif 100000000 < venta < 200000000:
                row.append("Mediana Empresa")
            else:
                row.append("Gran Empresa")
            empresas_dict["empresas"].append(
                {
                    "Rut":row[0],
                    "Nombre":row[1],
                    "Ventas":row[2],
                    "Clasificacion":row[3]
                }
            )
with open("Empresas.json", "w", ) as json_file:
    json.dump(empresas_dict, json_file)