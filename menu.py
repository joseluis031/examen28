import os
import helpers


def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido a Examen  ")
        print("========================")
        print("[1] Ejercicio 1 ")
        print("[2] Ejercicio 2   ")
        print("[3] Ejercicio 3   ")
        print("[4] Ejercicio 4")
        print("[5] Ejercicio 5")
        print("[6] Cerrar la clase de ecuaciones   ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Enunciado del ejercicio 1...\n")
            from ejercicios.Hanoi import hanoi,llenar_pilas

            n = int(input("Cant de discos:"))
       
            hanoi(n,1,2,3)
            llenar_pilas(n)

            

        elif opcion == '2':
            print("Enunciado del ejercicio 2...\n")
            import copy
            from ejercicios.matriz import matriz_iterativa,matriz_recursiva
            import copy
            print("el determinante de la matriz de forma recursiva es",matriz_recursiva([[3,5,8],[2,4,1],[2,0,7]]))
            
            print("el determinante de La matriz de forma iterativa es",matriz_iterativa([[3,5,8],[2,4,1],[2,0,7]]))

        elif opcion == '3':
            print("Enunciado del ejercicio 3...\n")
            from ejercicios.naves import ordenar,ordenar2,Halcon,Estrella,Mas_pasajeros,Mas_tripulantes,AT,pasajeros6,Mayor,Menor
            import csv

            with open("Naves.csv","r") as file:
                reader = csv.DictReader(file, delimiter=";") #leo csv
                lista = list(reader) #lo paso a lista para q las funciones sean mas faciles
                ordenar()
                ordenar2()
                Halcon()
                Estrella()
                Mas_pasajeros()
                Mas_tripulantes()
                AT()
                pasajeros6()
                Mayor()
                Menor()
                
            

        elif opcion == '4':
            print("Enunciado del ejercicio 4...\n")
            
            from ejercicios.tda_polinomio import Polinomio,agregar_termino,mostrar,restar,dividir,eliminar,determinar
              #duda como importa fichero q necesito en otro fichero para el menu       
            x_3= Polinomio()
            agregar_termino(x_3,3,1)
            x_2 = Polinomio()
            agregar_termino(x_2,2,1)
            print("Operacion restar")
            resta = restar(x_3,x_2)
            print(mostrar(resta))
            print("Operacion dividir")
            division = dividir(x_3,x_2)
            print(mostrar(division))
            print("Eliminacion")
            eliminar(x_2,1)
            print(mostrar(x_2))
            print("4 funcion")
            print(determinar(x_2,3))

        
        elif opcion == '5':
            print("Enunciado del ejercicio 5...\n")
            from ejercicios.hash import main,descifrar
            texto = input("Introduce el texto a cifrar:")

            main(texto)
            descifrar(texto)
        elif opcion == '6':
            print("Saliendo de la clase de ecuaciones...\n")
            break

        input("\nPresiona ENTER para continuar...")
        
