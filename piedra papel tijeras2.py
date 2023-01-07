import random
elecciónSalir = "Nada"
while elecciónSalir != "SALIR":
    print("Bienvenido al juego Piedra Papel Tijeras !")
    elecciónJugador = input("Escribe Piedra, Papel o Tijeras...")
    elección = ["Piedra", "Papel", "Tijeras"]
    elecciónAdversario = random.choice(elección)
    if elecciónJugador == "Piedra" and elecciónAdversario == "Papel":
        print("La hoja de papel del adversario ha cubierto tu piedra.")
        print("GAME OVER, has perdido !")
    elif elecciónJugador == "Piedra" and elecciónAdversario == "Piedra":
        print("Tu piedra y la de tu adversario se explotan la cabeza al correr.")
        print("IGUALDAD.")
    elif elecciónJugador == "Piedra" and elecciónAdversario == "Tijeras":
        print("Tu piedra aplasta las tijeras del adversario.")
        print("FELICITACIONES, has ganado !")
    elif elecciónJugador == "Papel" and elecciónAdversario == "Piedra":
        print("Tu hoja de papel cubre la piedra del adversario")
        print("FELICITACIONES, has ganado !")
    elif elecciónJugador == "Papel" and elecciónAdversario == "Papel":
        print("Tu hoja de papel y la del adversario se encuentran y se hacen el amor.")
        print("IGUALDAD.")
    elif elecciónJugador == "Papel" and elecciónAdversario == "Tijeras":
        print("Las tijeras del adversario cortan tu hoja de papel.")
        print("GAME OVER, has perdido !")
    elif elecciónJugador == "Tijeras" and elecciónAdversario == "Piedra":
        print("La piedra del adversario aplasta tus tijeras.")
        print("GAME OVER, has perdido !")
    elif elecciónJugador == "Tijeras" and elecciónAdversario == "Papel":
        print("Tus tijeras cortan la hoja de papel del adversario")
        print("FELICITACIONES, has ganado !")
    elif elecciónJugador == "Tijeras" and elecciónAdversario == "Tijeras":
        print("Tus tijeras y los del adversario se encuentran y deciden de hacerse la guerra.")
        print("IGUALDAD.")
    else:
        print("Lo siento, no has elegido Piedra, Papel o Tijeras !")

