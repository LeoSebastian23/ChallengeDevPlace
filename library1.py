import os
import random

def menu():
    i=6
    while i < 0 or i > 5:  
        print("1- Ejercicio 1")
        print("2- Ejercicio 2")
        print("3- Ejercicio 3")
        print("4- Ejercicio 4")
        print("5- Ejercicio 5")
        print("0- Fin app")
        i = int(input("Selecciones una de las opciones: "))
        from os import system
        system("cls")
    return i

#//////////////////////////////////////////////////////////////////////////////////////////////////////

def ejercicio1():
        n = int(input("Ingrese un numero: "))
        i = 2
        while i < n and n % i != 0:
            i+=1
        if i == n:
            print("El numero es primo.")
        else:
            print("El numero NO es primo.") 

#//////////////////////////////////////////////////////////////////////////////////////////////////////

def ejercicio2 ():
    psw = input("Ingrese una contraseña: ")
    contraseña = input("Ingrese nuevamente la contraseña:\n")
    i=1
    while i < 3 and contraseña != psw:
        os.system("cls")
        print("Contraseña incorrecta.")
        contraseña = input("Intentelo nuevamente:\n")
        i +=1
    if contraseña == psw:
            print("Felicitaciones, recordás tu contraseña.")
    else: 
        print("Tenes que ejercitar la memoria.")
    input("Presione una tecla para continuar...")

#//////////////////////////////////////////////////////////////////////////////////////////////////////

def ejercicio3 ():
    v = int(input("Ingrese el valor de hora del empleado: "))
    nom = input("Ingrese el nombre del empleado: ")
    ant = int(input("Ingrese la antiguedad del empleado en años: "))
    hrs = int(input("Cantidad de horas realizadas en el mes: "))

    tot = hrs * v 
    if ant >= 10:
        totAnt = ant * 30
        tot = totAnt + tot
    print("Empleado:", nom)
    print("Antiguedad: ",ant,"años")
    print("Total a cobrar: ", tot)

#//////////////////////////////////////////////////////////////////////////////////////////////////////

def ejercicio4():

    rnd = random.randint(1,1000)
    print("Se ha generado un numero aleatoriamente entre 1 y 1000.")
    print("Adivina cual es!")
    nro = int(input("nro: "))

    while nro != rnd:
        if nro < rnd:
            print("Es menor.")
            nro = int(input("Intentelo nuevamente: "))
        elif nro > rnd:
            print("Es mayor.")
            nro = int(input("Intentelo nuevamente: "))
    print("Acertaste!")

#//////////////////////////////////////////////////////////////////////////////////////////////////////

def ejercicio5():
    num = int(input("Ingrese un numero entero."))
    max = num
    min = num
    sum = num
    sumTot = 1

    while num != -1:
            num = int(input("Ingresa un conjunto de numeros a calcular. Para finalizar ingrese -1\n"))
            if num >= max and num != -1:
                max = num
            elif num <= min and num != -1:
                min = num 
    
            if num != -1:
                sum = num + sum
                sumTot +=1
    print("Mayor numero introducido: ",max)
    print("Menor numero introducido: ",min)
    print("Suma de todos los numeros: ",sum)
    print("Suma de los numeros: ",sumTot) 

#//////////////////////////////////////////////////////////////////////////////////////////////////////