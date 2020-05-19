#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para poner a prueba los conocimientos adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica numérica
    
    # Operadores con números decimales
    print('Ingrese el primer número decimal a operar:')
    numero_1 = int(input())

    numero_2 = int(input())
    
    # Alumno: Imprima en pantalla los dos números decimales solicitados
    print(numero_1, numero_2)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    eje_suma = numero_1 + numero_2
    print("El resultado de sumar",numero_1, "y", numero_2, "es",eje_suma)

    # Resta
    eje_resta = numero_1 - numero_2
    print("El resultado de restar",numero_1, "y", numero_2, "es",eje_resta)

    # División
    eje_division = numero_1 / numero_2
    print("El resultado de dividir",numero_1, "y", numero_2, "es",eje_division)

    # Multiplicación
    eje_multiplicacion = numero_1 * numero_2
    print("El resultado de multiplicar",numero_1, "y", numero_2, "es",eje_multiplicacion)

def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números reales
    print('Ingrese el primer número real a operar:')
    numero_3 = float(input())

    print('Ingrese el segundo número real a operar:')
    numero_4 = float(input())

    print("El primer número ingresado es",numero_3,"El segundo número ingresaso es",numero_4)

    # Alumno: Imprima en pantalla los dos números reales solicitados
    # print(....)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_3, numero_4
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    suma_1 = numero_3 + numero_4
    print("El resultado de sumar",numero_3,"y",numero_4,"es",suma_1)
    
    # Resta
    resta_1 = numero_3 - numero_4
    print("El resultado de restar",numero_3,"y",numero_4,"es",resta_1)

    # División
    division_1 = numero_3 / numero_4
    print("El resultado de división",numero_3,"y",numero_4,"es",division_1)

    # Multiplicación
    multi_1 = numero_3 * numero_4
    print("El resultado de multiplicar",numero_3,"y",numero_4,"es",multi_1)

def ej33():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    nombre_y_apellido = nombre + " " + apellido
        
    # Imprima su nombre completo
    print(nombre_y_apellido)

    # Almacenar su nombre completo en una variable
    
    # nombre_completo = .....

    # Imprimir la cantidad de letras que posee su nombre completo
    letras_1 = len(nombre_y_apellido)
    letras_1 = letras_1-1
    print(letras_1)

def ej3():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    acro1 = palabra_1[0]
    acro2 = palabra_2[0]
    acro3 = palabra_3[0]

    print(acro1+acro2+acro3)

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla

def ej4():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    # Formar una nueva palabra con los recortes solicitados
    # Imprima en pantalla los resultados

    recorte_1 = palabra_1[:3]
    recorte_2 = palabra_2[-3:]

    print(recorte_1)
    print(recorte_2)
    print(recorte_1 + recorte_2)
    
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej33()
