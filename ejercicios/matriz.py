#matriz recursiva

def matriz_recursiva(matriz):
    suma=0
    
    if len(matriz) == 3 and len(matriz[0])==3:
        suma = ((matriz[0][0] * matriz[1][1] * matriz[2][2])+(matriz[1][0] * matriz[2][1]*matriz[0][2]) +(matriz[0][1] * matriz[1][2] * matriz[2][0]))-(matriz[0][2] * matriz[1][1] * matriz[2][0] )-(matriz[0][1]*matriz[1][0]*matriz[2][2])-(matriz[1][2] * matriz[2][1] * matriz[0][0])