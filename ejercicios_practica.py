#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un calculadora, se ingresará por línea de comando dos números reales
    y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia
    
    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
    num_1 = float(input("Ingrese el primer número: "))
    num_2 = float(input("Ingrese el segundo número: "))

  #Operaciones matemáticas

  #Suma
    suma_1 = num_1 + num_2
    print("La suma entre", num_1,"y",num_2,"es",suma_1)

  #Resta
    resta_1 = num_1 - num_2
    print("La resta entre", num_1,"y",num_2,"es",resta_1)

  #Multiplicación
    multi_1 = num_1 * num_2
    print("La multiplicación entre", num_1,"y",num_2,"es",multi_1)

  #División
    division_1 = num_1 / num_2
    print("La división entre", num_1,"y",num_2,"es",division_1)

  #Exponente / Potencia
    potencia_1 = num_1 ** num_2
    print("La potencia entre", num_1,"y",num_2,"es",potencia_1)

def ej2():
    # Ejercicios de práctica numérica y cadenas
    
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea entienda de que se
      está hablando.

    '''
    nombre_completo = str(input("Ingrese su nombre completo: "))
    documento = float(input("Ingrese su numero de DNI: "))
    edad = int(input("Ingrese su edad: "))
    estatura = float(input("Ingrese su altura: "))

    print("Nombre Completo: ",nombre_completo,"con DNI",documento)
    print("Nombre Completo: ",nombre_completo,"Edad: ",edad,"y",estatura,"de altura")

def ej3():
    # Ejercicios de práctica con cadenas

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar el método "split"
    Mostraremos un ejemplo:
    
    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método que seguramente
    utilizarán mucho de acá en adelante. Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
        
    '''
    nombre_padre_1 = str(input("Ingrese el nombre del primer padre: "))
    nombre_padre_2 = str(input("Ingrese el nombre del segundo padre: "))
    nombre_hijo = str(input("Ingrese el nombre del hijo: "))

    nombre_padre_1.split(" ")
    nombre_padre_2.split(" ")

    nombre_1,nombre_2 = nombre_padre_1.split(" ")
    nombre_3,nombre_4 = nombre_padre_2.split(" ")

    print(nombre_hijo + " " + nombre_2 + " " + nombre_4)

def ej4():
    # Ejercicios de práctica con cadenas

    '''
    Realice un programa que determine si una persona_2 es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir, primero el nombre y luego
    el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido en el nombre completo
      de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método que seguramente
    utilizarán mucho de acá en adelante. Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
            
    '''
    persona_1 = str(input("Ingrese un nombre y apellido: "))
    persona_2 = str(input("Ingrese un nombre y apellido: "))

    nombre_1,apellido_1 = persona_1.split(" ")
    nombre_2,apellido_2 = persona_2.split(" ")

    apellido = apellido_2

    print(apellido in persona_1)

def ej5():
    # Ejercicios de práctica con cadenas
       
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos un el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    

    '''
    nombre_completo = str(input("Ingrese su nombre completo: "))

    print(nombre_completo.lower())
    print(nombre_completo.upper())
    print(nombre_completo.capitalize())
    
if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
