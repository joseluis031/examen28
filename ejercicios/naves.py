import csv

with open("Naves.csv","r") as file:
    reader = csv.DictReader(file, delimiter=";") #leo csv
    lista = list(reader) #lo paso a lista para q las funciones sean mas faciles
    
def ordenar():
    orden = []
    for i in lista:
        orden.append(i["Nombre"])
    a = sorted(orden)
    print("Las naves ordenadas son: ",a)
    
ordenar()

def ordenar2():
    orden = []
    for i in lista:
        orden.append(i["Largo"])
    orden.sort(reverse=True)
    print("Las naves ordenadas de mayor a menor por su largo son: ",orden)
    
ordenar2()

def Halcon():
    halcon = []
    for i in lista:
        if i["Nombre"] == "Halcon Milenario":
            halcon.append(i)
    print(halcon)  
Halcon()

def Estrella():
    estrella = []
    for i in lista:
        if i["Nombre"] == "Estrella de la Muerte":
            estrella.append(i)
    print(estrella)  
Estrella()

def Mas_pasajeros():
    pasj = []
    for i in lista:
        pasj.append(i["Pasajeros"])
    pasj.sort(reverse=False)
    top3 = pasj[2:5]
    print("Top 3 naves que necesitas mas pasajeros:",top3)
    
Mas_pasajeros()


def Mas_tripulantes():
    trip = []
    for i in lista:
        trip.append(i["Tripulacion"])
    for i in lista:
        if i["Tripulacion"] == max(trip):
            print(i["Nombre"],"con",i["Tripulacion"])
        
Mas_tripulantes()
    
def AT():
    at = []
    for i in lista:
        at.append(i["Nombre"])
    if "AT" in at:
            print(at)
    else:
            print("No existe nave que tenga AT")
            
AT()

def pasajeros6():
    pas = []
    for i in lista:
        if int(i["Pasajeros"]) >=6:
            pas.append(i["Nombre"])
        else:pass
    print("Las naves q pueden llevar 6 o mas son:",pas)
    
pasajeros6()

def Mayor():
    mayor = []
    for i in lista:
        mayor.append(i["Largo"])
    for i in lista:
        if i["Largo"] == max(mayor):
            print(i)
            
Mayor()

def Menor():
    menor = []
    for i in lista:
        menor.append(i["Largo"])
    for i in lista:
        if i["Largo"] == min(menor):
            print(i)
            
Menor()