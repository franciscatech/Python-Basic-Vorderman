sujeto = ["Nina", "Luis", "José"]
verbo = ["compra", "cabalga", "golpea"]
nombre = ["león", "bicicleta", "avión"]
from random import randint
def escog(palabras):
    num_palabras = len(palabras)
    num_eleg = randint(0, num_palabras - 1)
    palabra_eleg = palabras[num_eleg]
    return palabra_eleg
print(escog(sujeto), escog(verbo), "un/una", escog(nombre), end=".\n")

#Ahora vamos a hacer que este programa sea infinito con un bucle.

while True:
    print(escog(sujeto), escog(verbo), "un/una", escog(nombre), end=".")
    input

#Para detenerlo, pulsaremos CTRL+C.
