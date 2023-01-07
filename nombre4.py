import random
nombre = random.randint(1,100000)
deviner = int(input("Je pense à un nombre entre 1 et 100 000. Lequel est-ce ?"))
while deviner != nombre:
    if deviner < nombre:
        print("Ton nombre est trop bas...")
    else:
        print("Ton nombre est trop élevé...")
    deviner = int(input("Essaie à nouveau..."))
print("Félicitations ! Bonne réponse !")
