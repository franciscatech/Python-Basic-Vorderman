from turtle import *
forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(120)
for i in range(3):
    forward(100)
    right(120)
for i in range(2, 11, 2):
    print(i, end=" ")
for i in range(10):
    print(i, end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")
n = 3
for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(b, "x", a, "=", b * a)
n = 3
for a in range(1, n + 3):
    for b in range(1, n + 3):
        print(b, "x", a, "=", b * a)
respuesta = "s"
while respuesta == "s":
    print("Quédate muy quieto.")
    respuesta = input("¿El monstruo es amigo? (s/n)")
print("¡Huye!")
intentos = 0 #Primero definimos la variable para que el bucle sepa por donde empezar.
while intentos < 3:
    respuesta = input("Teclea una palabra: ")
    print("Por favor no teclees \"" + respuesta + "\" otra vez.")
    intentos += 1 #Esto hace que el bucle avance hasta llegar a 3
#Ahora el programa sigue en esta parte
table = 7
for i in range(1, 13):
    print("¿Cuánto es", i, "x", table, "?")
    calculo = input()
    if calculo == "stop":
        break #Aquí modificamos el código para introducir un bucle de escape.
    if calculo == "skip":
        print("Pasando")
        continue #Aquí modificamos el código para hacer skipping.
    respuesta = i * table
    if int(calculo) == respuesta:
        print("¡Correcto!")
    else:
        print("No, es", respuesta)
print("Acabado")

#Ejercicios de código sobre los bucles de Python. 
