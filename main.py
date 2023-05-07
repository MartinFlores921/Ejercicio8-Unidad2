"""  
Ejercicio 8
Sobrecarga de operadores

Defina una clase “Conjunto” que represente un conjunto matemático de números enteros.

Implemente un programa que presente un menú de opciones que permita lo siguiente:

1- La unión de dos conjuntos, para ello sobrecargue el operador binario suma (+). 
Teniendo en cuenta que la unión es un nuevo conjunto que posee los elementos de ambos conjuntos, 
en caso de haber elementos repetidos solo aparecen una vez en el resultado. Ejemplo: Sea A={1,2,3,4} 
y B= {3,6,9}, A+B = {1,2,3,4,6,9}

2- La diferencia de dos conjuntos, para ello sobrecargue el operador binario resta (-).
Teniendo en cuenta que el resultado de la diferencia de conjuntos es un nuevo conjunto que posee los elementos del primer operando que no se encuentren en el segundo operando.
Ejemplo: Sea A={1,2,3,4} y B= {3,6,9}, A-B = {1,2}

3- Verificar si dos conjuntos son iguales, para ello sobrecargue el operador “==” teniendo en cuenta que dos conjuntos se consideran iguales si tienen la misma cantidad de elementos y sus valores son iguales
(sin importar el orden de los elementos)



""" 
from Conjunto import conjunto
if __name__=='__main__':
    conjunto1= conjunto([1,2,3,4])
    conjunto2= conjunto([3,6,9])
    op=int(input("\n1- A + B\n2- A - B\n3- A = B\nIngrese una opcion (0 Para terminar): "))
    while op != 0:
        print("A: {}".format(conjunto1))
        print("B: {}".format(conjunto2))
        if op == 1:
            print("A+B= {}".format(conjunto1 + conjunto2))
        elif op == 2:
            print("A-B = {}".format(conjunto1 - conjunto2))
        elif op == 3:
            print("A=B : {}".format(conjunto1 == conjunto2))
        op = int(input("\n1- A + B\n2- A-B\n3-A=B\nIngrese una opcion (0 Para terminar): "))
    print("--FIN--") 