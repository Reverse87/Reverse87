import random
print("Je vais lancer les dés. ")
nombre = int(input("Donnez un chiffre entre 2 et 12 : "))
if nombre == random.randint(2,12):
    print("Tu as gagné !")
else:
    print("Tu as perdu !")
