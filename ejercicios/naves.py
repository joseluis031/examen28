import csv

with open("Naves.csv","r") as file:
    reader = csv.DictReader(file,delimeter=";") #leo csv
    lista = list(reader) #lo paso a lista para q las funciones sean mas faciles
    
def ordenar():
    orden = []
    for i in lista:
        orden.append(i["Nombre"])
    a = sorted(orden)
    print("Las naves ordenadas son: ",a)
    
ordenar()
    