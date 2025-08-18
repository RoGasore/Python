eleves = {}

def ajouter_eleve():
    for i in range(1000): 
        id_eleve = f"E00{i+1}"
        nom = input("NOM : ").upper()
        post_nom = input("POST-NOM : ").upper()
        prenom = input("PRENOM : ").title()
        classe = input("CLASSE : ").lower()
        option = input("OPTION : ").lower()

        eleves [id_eleve] = {
            "nom" : nom,
            "post_nom" : post_nom,
            "prenom" : prenom,
            "classe" : classe,
            "option" :option
        }
        print(f"L'élève {nom} {post_nom} {prenom} a été bien enregistré(e).")

        choix = ["q", "n"]
        while True :
            quitter = input("Appuyer sur \n Q: Pour quitter \n N: Pour continuer \n").lower()
            if quitter not in choix == "n" or "q" :
                break
            else :
                print("Veuillez saisir un caractère autorisé")
                continue
        if quitter == "n" :
            continue
        elif quitter == "q" :
            break
        else :
            print("Error.......\n")
            
ajouter_eleve()
