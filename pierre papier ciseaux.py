import random
print("Bienvenue au jeu Pierre Papier Ciseaux !")
choixJoueur = input("Écrivez Pierre, Papier ou Ciseaux...")
choix = ["Pierre", "Papier", "Ciseaux"]
choixAdversaire = random.choice(choix)
if choixJoueur == "Pierre" and choixAdversaire == "Papier":
    print("La feuille de papier de l'adversaire recouvre votre pierre.")
    print("GAME OVER, vous avez perdu !")
elif choixJoueur == "Pierre" and choixAdversaire == "Pierre":
    print("Votre pierre et celle de l'adversaire se percutent la tronche.")
    print("ÉGALITÉ.")
elif choixJoueur == "Pierre" and choixAdversaire == "Ciseaux":
    print("Votre pierre écrase les ciseaux de l'adversaire.")
    print("BRAVO, vous avez gagné !")
elif choixJoueur == "Papier" and choixAdversaire == "Pierre":
    print("Votre feuille de papier recouvre la pierre de l'adversaire.")
    print("BRAVO, vous avez gagné !")
elif choixJoueur == "Papier" and choixAdversaire == "Papier":
    print("Votre feuille de papier et celle de l'adversaire se rencontrent et se font l'amour.")
    print("ÉGALITÉ.")
elif choixJoueur == "Papier" and choixAdversaire == "Ciseaux":
    print("Les ciseaux de l'adversaire découpent votre feuille de papier.")
    print("GAME OVER, vous avez perdu !")
elif choixJoueur == "Ciseaux" and choixAdversaire == "Pierre":
    print("La pierre de l'adversaire écrase vos ciseaux.")
    print("GAME OVER, vous avez perdu !")
elif choixJoueur == "Ciseaux" and choixAdversaire == "Papier":
    print("Vos ciseaux découpent la feuille de papier de l'adversaire.")
    print("BRAVO, vous avez gagné !")
elif choixJoueur == "Ciseaux" and choixAdversaire == "Ciseaux":
    print("Vos ciseaux et ceux de l'adversaire se rencontrent et décident de s'entretuer saperlipopette.")
    print("ÉGALITÉ.")
else:
    print("Désolé, vous n'avez pas entré Pierre, Papier ou Ciseaux !")
print("Lancez à nouveau le jeu pour réésayer.")
