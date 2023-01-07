import random
nombre = random.randint(2, 12)
deviner = int(input("Je vais lancer les dés. Donnez un chiffre entre 1 et 12 : "))
while deviner != nombre:
    if deviner < nombre:
        print("Tu as perdu !")
    else:
        print("Tu as perdu !")
    deviner = int(input("Essaie à nouveau..."))
print("Tu as gagné !")
