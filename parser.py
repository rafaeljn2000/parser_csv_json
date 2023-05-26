import csv
import json

#nombres de los archivos por abrir y a convertir
csv_archivo = 'cities.csv'
json_archivo = 'cities.json'

# funcion que abre archivo CSV, lo lee y lo almacena en una lista y posteriormente lo guarda en archivo JSON

def csv_to_json(csv_archivo, json_archivo):
    # Abrir CSV en modo lectura
    with open(csv_archivo, 'r') as file:
        # Leer el archivo CSV
        datos_csv= csv.DictReader(file)
        
        # Convertir CSV a  diccionarios
        lista_datos = []
        for row in datos_csv:
            lista_datos.append(row)
    
    # Abrir el archivo JSON en modo escritura
    with open(json_archivo, 'w') as file:
        # Escribir  JSON en el archivo
        json.dump(lista_datos, file, indent=4)



# Se manda a llamar a la funcion
csv_to_json(csv_archivo, json_archivo)

print("La conversion se realizo con exito")
