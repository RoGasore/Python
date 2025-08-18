import random

nbre_mystere = random.randint(1, 100)
nbre_essais = 5
print("Bienvenue dans le jeu du nombre mystère !")
print("Vous avez", nbre_essais, "essais pour trouver le nombre.")
nbre_saisie = input("Devine le nombre :")

while not nbre_saisie.isdigit():
    print("Veuillez entrer un nombre valide.")
    nbre_saisie = input("Devine le nombre :")

while nbre_essais > 0:
        nbre_saisie = int(nbre_saisie)
        if nbre_saisie == nbre_mystere:
            print("Bravo ! Vous avez trouvé le nombre mystère :", nbre_mystere, "\n Après", i, "essais.")
            break
        elif nbre_saisie < nbre_mystere:
            print("Trop petit !")
            continue
        elif nbre_saisie > nbre_mystere:
            print("Trop grand !")
            continue
        else:
            print("Veuillez entrer un nombre valide.")
            nbre_saisie = input("Devine le nombre :")
        i=-1

#continuer = 'o'
#while continuer == 'o' :
#    print("Continuer")
#    continuer = input("Voulez-vous continuer ? o/n ")
#    if continuer == 'n':
#        print("Fin de la boucle")
#       break;