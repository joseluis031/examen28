#matriz recursiva
import copy
def matriz_recursiva(matriz):
    suma=0
    
    if len(matriz) == 3 and len(matriz[0])==3: #columnas y filas
        suma = ((matriz[0][0] * matriz[1][1] * matriz[2][2])+(matriz[1][0] * matriz[2][1]*matriz[0][2]) +(matriz[0][1] * matriz[1][2] * matriz[2][0]))-(matriz[0][2] * matriz[1][1] * matriz[2][0] )-(matriz[0][1]*matriz[1][0]*matriz[2][2])-(matriz[1][2] * matriz[2][1] * matriz[0][0]) #calcular el determinante
        
        return suma
    
    else:
        for i in range(len(matriz)):
            aux = copy.deepcopy(matriz)
            aux.remove(matriz[0])
            for j in range(len(aux)):
                aux[j] = aux[j][0:1]+aux[j][i+1] #creo submatrices
            suma += (-1)**(i%2)*matriz[0][i]*matriz_recursiva(aux)
        return suma
    
print(matriz_recursiva([[3,5,8],[2,4,1],[2,0,7]]))  #3x3


#matriz iterativa
def matriz_iterativa(matriz):
    suma = 0
    for i in range(3): #3x3
        suma = ((matriz[0][0] * matriz[1][1] * matriz[2][2])+(matriz[1][0] * matriz[2][1]*matriz[0][2]) +(matriz[0][1] * matriz[1][2] * matriz[2][0]))-(matriz[0][2] * matriz[1][1] * matriz[2][0] )-(matriz[0][1]*matriz[1][0]*matriz[2][2])-(matriz[1][2] * matriz[2][1] * matriz[0][0]) #calcular el determinante
        
    return suma

print(matriz_iterativa([[3,5,8],[2,4,1],[2,0,7]]))
