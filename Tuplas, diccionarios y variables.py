#Tuplas 
dragonA = ("José", 15, 1.70)
dragonB = ("Laura", 16, 1.68)
nombre, edad, altura = dragonA
print(nombre, edad, altura)
nombre, edad, altura = dragonB
print (nombre, edad, altura)
dragones = [dragonA, dragonB]
print(dragones)

#Diccionarios
edad = {"Maria": 10, "Santi": 8, "Diego": 18, "Victoria": 20}
print(edad)
edad["Óscar"] = 11
print(edad)
edad["Óscar"] = 12
print(edad)
del edad["Óscar"]
print(edad)

#Listas en variables
a = 2
b = a
print("a =", a, "b =", b)

a = 100
print("a =", a, "b =", b)

b = 22
print("a =", a, "b =", b)

listaA = [1, 2, 3]
listaB = listaA
print("listaA =", listaA, "listaB =", listaB)

listaA[1] = 1000
print("listaA =", listaA, "listaB =", listaB)

listaB[2] = 75
print("listaA =", listaA, "listaB =", listaB)

#Vasiables y funciones
def func1():
    a = 10
    print(a)

b = 100
def func2():
    print(b)

def func3(y):
    print(y)
    y = "pan"
    print(y)
z = "mantequilla"
func3(z)

c = 12345
def func4():
    c = 555
    print(c)
