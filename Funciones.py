def saludo():
    print("¡Hola!")

def altura(m, cm):
    total = (100 * m) + cm
    print(total, "cm de altura")

def num_input(prompt):
    tecleado = input(prompt)
    num = int(tecleado)
    return num

a = num_input("Introduce a")
b = num_input("Introduce b")
print("a + b =", a + b)
