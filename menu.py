import os
import random

'''
n = int(input("Ingrese un numero: "))
i = 2
while i < n and n % i != 0:
    i+=1
if i == n:
    print("El numero es primo.")
else:
    print("El numero NO es primo.") 

'''

'''
psw = input("Ingrese una contraseña: ")
contraseña = input("Ingrese nuevamente la contraseña:\n")
i=1
while i < 3:
    os.system("cls")
    if contraseña != psw:
        print("Contraseña incorrecta.")
        contraseña = input("Intentelo nuevamente:\n")
    i +=1
if contraseña == psw:
        print("Felicitaciones, recordás tu contraseña.")
        input("Presione una tecla para continuar...")
else: 
    print("Tenes que ejercitar la memoria.")
    input("Presione una tecla para continuar...")
'''
'''
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
'''

'''
min = 1
max = 1000

rnd = random.randint(1,1000)
print("Se ha generado un numero aleatoriamente entre 1 y 1000.")
print("Adivina cual es!")
nro = int(input("nro: "))
intentos = 1
while nro != rnd:
    if nro < rnd:
        print("Es menor.")
        nro = int(input("Intentelo nuevamente: "))
    elif nro > rnd:
        print("Es mayor.")
        nro = int(input("Intentelo nuevamente: "))
print("Acertaste!")
'''
n = []
m = 1

while m != -1:
    n.append(int(input("Ingrese un numero: ")))
    m= int(input("Para continuar ingrese una tecla cualquiera\nPara finalizar ingrese [-1] "))
