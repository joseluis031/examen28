import hashlib
def main(texto):
    
    
    cifrar = hashlib.sha256(texto.encode("utf-8")).hexdigest()
    print(cifrar)

def descifrar(texto):
    texto2 = input("introduce el texto a descifrar:")
    cifrar = hashlib.sha256(texto.encode("utf-8")).hexdigest()
    if texto2 == cifrar:
        print("Mensaje correcto:",texto)
    else:
        print("El mensaje no coincide") 
        pass
        

    