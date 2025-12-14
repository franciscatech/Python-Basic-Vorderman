#Vamos a ver los tipos de datos que manejamos en Python

print("integer")
ovejas = 1
print(ovejas)
print("float")
ovejas = 1.5
print(ovejas)
print("string")
a = "¡Programar con Python es divertido!"
print(a)
print("booleanos")
a = True
print(a)
a = False
print(a)


#Vamos a hacer cálculos sencillos con Python

hormigas = 22
arañas = 35
bichos = hormigas + arañas
print(bichos)

manzanas = 55
niños = 5
merienda = manzanas / niños
print(merienda)

zapatillas = 12
calcetines = 4
desparejados = zapatillas - calcetines
print(desparejados)

bombones = 22
cajas = 16
dulces = bombones * cajas
print(dulces)


#Vamos a trabajar con las cadenas en Python

a = "¡Corre!"
b = "Llegan los alienigenas"
c = a + b
print(c)

c = b + "¡Cuidado!" + a
print(c)

#El siguiente código funciona en la shell
a = "DICIEMBRE"
a[3]
a[1:6]
a[:4]
a[5:]


#Vamos a trabajar con input y output
nombre = input ("Introduce tu nombre:")
print("Hola", nombre)

a = "Dani"
b = "tiene"
c = 12
print(a, b, c, end=".")
print("Adiós", a)
print(a, b, c, sep="-")
print(a, b, c, sep="\n")


#Vamos a tomar decisiones en Python. Este código funciona en la shell
juguetes = 10
juguetes == 1
juguetes > 1
juguetes < 1
juguetes != 1
juguetes <= 1
not juguetes == 1
juguetes == 9 or juguetes == 10
juguetes == 9 and juguetes == 10

dia = 28
mes = 7
dia == 28 and mes == 7
dia = 28
mes = 7
not (dia == 28 and \
     mes == 7)

dia = 28
mes = 7
(dia == 28 and mes == 7) \
     or (dia == 1 and mes == 1)

#Vamos a ramificar en Python
respuesta = input("¿Es tu cumpleaños? (s/n)")
if respuesta == "s":
    print("¡Feliz cumpleaños!")

respuesta = input("¿Es Año Nuevo? (s/n)")
if respuesta == "s":
    print("¡Feliz Año Nuevo!")
    print("Es hora de los fuegos artificiales.")
else:
    print("¡Aún no!")

a = int(input("a = "))
b = int(input("b = "))
op = input("suma/res/mul/div:")
if op == "suma":
    c = a + b
elif op == "res":
    c = a - b
elif op == "mul":
    c = a * b
elif op == "div":
    c = a / b
else:
    c = "Error"
print("Respuesta = ",c)
