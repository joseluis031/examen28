from codigo_pilas import *
torre1 = Pila() #pila vacia
torreaux = Pila()   #pila vacia
torre2 = Pila() #pila vacia


def crear_disco(n):
    torre = [[]]
    copia_n=n
    
    for i in range(2*n+3):  #posicion 0 de la matriz
        if i==(2*n+3)//2:
            torre[0].append("i")
        else:
            torre[0].append(" ")
            
            
    for i in range(1,n+1):
        torre.append([])
        for j in range(2*n+3):
            if j < copia_n -1 or j> (2*i+copia_n+1):
                torre[i].append(" ")
                
            elif j==copia_n-1:
                torre[i].append("[") #bordes torre
            elif j==(2*i+copia_n+1):
                torre[i].append("]")
            else:
                torre[i].append("=")
                
        copia_n-=1
        
def llenar_pilas(n):
    for i in range(n, -1,-1):
        torre1.apilar(i)
        torreaux.apilar(0)
        torre2.apilar(0)
        print(torre1(),torre2(),torreaux())
    torre1.puntero=n
    torreaux.puntero=0
    torre2.puntero=0
    print(torre1,torre2,torreaux)





def hanoi(n,inicio,final,aux):
    if n == 1:
        print(inicio,"---",final)
    else:
        hanoi(n-1,inicio,aux,final) #aux y final al reves
        print(inicio,"---",final)
        hanoi(n-1,aux,final,inicio)  #origen y dest


n = int(input("Cant de discos:"))
       
hanoi(n,1,2,3)
llenar_pilas(n)
