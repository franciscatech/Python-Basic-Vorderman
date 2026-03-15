
from turtle import *

# ==========================================
# PARTE 1: Dibujo inicial automático
# ==========================================
reset()
speed(3)
left(90)
forward(100)
right(45)
forward(70)
right(90)
forward(70)
right(45)
forward(100)
right(90)
forward(100)

# ==========================================
# PARTE 2 Y 3: La Máquina de Dibujar
# ==========================================

def controlador_de_tortuga(do, val):
    do = do.upper()
    if do == "F": forward(val)
    elif do == "B": backward(val)
    elif do == "R": right(val)
    elif do == "L": left(val)
    elif do == "U": penup()
    elif do == "D": pendown()
    elif do == "N": reset()
    else: print("Comando desconocido:", do)

def artista_de_cadena(program):
    # Esta es la versión corregida que no falla con espacios o comillas
    lista_comando = program.split("-")
    for comando in lista_comando:
        comando = comando.strip().replace('"', '').replace("'", "")
        if len(comando) < 1: continue
        
        tipo_comando = comando[0]
        try:
            # Extrae el número después de la letra
            num = int(comando[1:]) if len(comando) > 1 else 0
            print(f"Ejecutando: {tipo_comando} {num}")
            controlador_de_tortuga(tipo_comando, num)
        except ValueError:
            print(f"Error: '{comando}' no tiene un número válido.")

# --- CONFIGURACIÓN DE LA VENTANA ---
shape("turtle")
print("\n--- MÁQUINA DE DIBUJAR LISTA ---")
print("Escribe comandos en la consola (Ejemplo: F50-R90-F50)")
print("Escribe 'salir' para terminar.")

# --- BUCLE DE CONTROL ---
while True:
    try:
        instrucciones = input("Introduce comandos: ")
        
        if instrucciones.lower() == 'salir':
            print("Cerrando...")
            break # Rompe el bucle para llegar al final
            
        artista_de_cadena(instrucciones)
        
    except EOFError: # Por si se corta la entrada
        break
    except Terminator:
        print("Ventana cerrada.")
        break

print("Programa finalizado.")
