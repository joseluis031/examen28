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
            import sympy as sp
            from Clase.ejercicio import Ecuacion1
            x = sp.Symbol("x")
            y = sp.Function("y")

            a = y(x).diff(x)
            sol1 = Ecuacion1(x,y,a)
            print(sol1)
            sol1.resolver()

        elif opcion == '2':
            print("Enunciado del ejercicio 2...\n")
            import sympy as sp
            from Clase.ejercicio2 import Ecuacion2
            x = sp.Symbol("x")
            y = sp.Function("y")
            
            sol2 = Ecuacion2(x,y,a)
            print(sol2)
            sol2.resolver()

        elif opcion == '3':
            print("Enunciado del ejercicio 3...\n")
            import sympy as sp
            from Clase.ejercicio3 import Ecuacion3
            x = sp.Symbol("x")
            y = sp.Function("y")
            
            sol3 = Ecuacion3(x,y,a)
            print(sol3)
            sol3.resolver()
            

        elif opcion == '4':
            print("Enunciado del ejercicio 4...\n")
            import sympy as sp
            from Clase.ejercicio4 import Ecuacion4
            x = sp.Symbol("x")
            y = sp.Function("y")
            
            sol4 = Ecuacion4(x,y,a)
            print(sol4)
            sol4.resolver()

        
        elif opcion == '5':
            print("Saliendo de la clase de ecuaciones...\n")
            break

        input("\nPresiona ENTER para continuar...")