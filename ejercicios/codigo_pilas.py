class nodoPila(object):
    #Clase nodo pila
    info, sig = None, None

class Pila(object):
    #clase pila

    def __init__(self):
        #crea una pila vacia
        self.cima = None
        self.tamanio = 0

def apilar(pila, dato):
        #apila el dato sobre la cima de la pila
        nodo = nodoPila()  #se debe crear esta variable
        nodo.info = dato    #se le asigna info(el valor del elemento ingresado como dato)
        nodo.sig = pila.cima  #en el campo siguiente se guarda la direccion de referencia de la cima
        pila.cima = nodo      #a la cima se le asigna la direccion del nodo cread0
        pila.tamanio += 1    #se aumenta el tamaño

def desapilar(pila):
        #desapila el elemento en la cima de la pila y te devuelve
        x = pila.cima.info    #se saca la informacion del nodo q esta en la cima (y se alamcena en variable auxiliar)
        pila.cima = pila.cima.sig #a la cima se le asigna la direccion de referencia almacenada en el atributo siguiente del nodo de la cima(el q esta justo abajo)
        pila.tamanio -= 1     #y ya como la cima a pasado a ser el nodo anterior, el tamaño decrece
        return x   #se retorna el valor de la variable auxiliar(elemento eliminado)

def pila_vacia(pila):
    #Devuelve true si la pila está vacia
    return pila.cima is None

def en_cima(pila):
    #Devuelve el valor almacenado en la cima de la pila
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None

def tamanio(pila):
    #devuelve el numero de elementos en la pila
    return pila.tamanio

def barrido(pila):
    "Muestra el contenido de una pila sin perder datos"
    paux = Pila()  #pila auxiliar
    while (not pila_vacia(pila)): #mientras q la primera pila no este vacia
        dato = desapilar(pila)   #se vacia
        print(dato)              
        apilar(paux, dato)       #funcion de apilar pero en la pila auxiliar con los datos q teniamo en la otra pila
    while (not pila_vacia(paux)): #para volver a reconstruir la pila principal, mientras q la auxiliar no este vacia
        dato = desapilar(paux)   #se vacia
        apilar(pila, dato)        #se contruye de nuevo la primera pila con los datos q paso a tener la auxiliar