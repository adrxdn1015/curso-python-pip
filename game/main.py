import random

def jugar_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]

    jugador = input("Elige piedra, papel o tijeras: ").lower()
    computadora = random.choice(opciones)

    print(f"Jugador elige: {jugador}")
    print(f"Computadora elige: {computadora}")

    if jugador in opciones:
        if jugador == computadora:
            resultado = "Empate"
        elif (
            (jugador == "piedra" and computadora == "tijeras") or
            (jugador == "papel" and computadora == "piedra") or
            (jugador == "tijeras" and computadora == "papel")
        ):
            resultado = "¡Ganaste!"
        else:
            resultado = "La computadora gana"
    else:
        resultado = "Opción no válida. Por favor, elige piedra, papel o tijeras."

    print(resultado)

if __name__ == "__main__":
    jugar_piedra_papel_tijeras()
