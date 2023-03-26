import random

print("Bienvenido al juego de Piedra, Papel o Tijera")

opciones = ["piedra", "papel", "tijera"]

while True:
    # Elige una opción al azar para la computadora
    computadora = random.choice(opciones)
    
    # Pide al usuario que seleccione una opción
    usuario = input("Elige piedra, papel o tijera: ").lower()
    print(f"La computadora elige: {computadora}")
    
    # Comprueba si la opción del usuario es válida
    if usuario not in opciones:
        print("Opción no válida. Inténtalo de nuevo.")
        continue
    
    # Comprueba quién ganó
    if usuario == "piedra" and computadora == "tijera":
        print("Ganaste! La piedra aplasta las tijeras.")
    elif usuario == "tijera" and computadora == "papel":
        print("Ganaste! Las tijeras cortan el papel.")
    elif usuario == "papel" and computadora == "piedra":
        print("Ganaste! El papel envuelve la piedra.")
    elif usuario == computadora:
        print("Empate!")
    else:
        print("Perdiste! La computadora eligió", computadora)
    
    # Preguntar si el usuario quiere jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo != "s":
        break

print("¡Gracias por jugar!")
