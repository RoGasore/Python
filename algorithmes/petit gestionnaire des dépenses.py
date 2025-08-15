# Gestion de dépenses en Python
# Permet d'ajouter, afficher, totaliser et filtrer des dépenses

def ajouter_depense(depenses, montant, categorie):
    #Ajoute une dépense à la liste
    depenses.append({'montant': montant, 'categorie': categorie})
    
def afficher_depenses(depenses):
    #Affiche toutes les dépenses
    for depense in depenses:
        print(f'Montant: {depense["montant"]}, Catégorie: {depense["categorie"]}')
    
def total_depenses(depenses):
    # Retourne la somme de toutes les dépenses
    return sum(map(lambda depense: depense['montant'], depenses))
    
def filtrer_depenses_par_categorie(depenses, categorie):
    #Retourne uniquement les dépenses correspondant à une catégorie donnée
    return filter(lambda depense: depense['categorie'] == categorie, depenses)
    

def main():
    depenses = []
    while True:
        print('\n--- Gestionnaire de Dépenses ---')
        print('1. Ajouter une dépense')
        print('2. Lister toutes les dépenses')
        print('3. Afficher le total des dépenses')
        print('4. Filtrer les dépenses par catégorie')
        print('5. Quitter')
       
        choix = input('Entrez votre choix: ')

        if choix == '1':
            montant = float(input('Entrez le montant: '))
            categorie = input('Entrez la catégorie: ')
            ajouter_depense(depenses, montant, categorie)

        elif choix == '2':
            print('\nToutes les dépenses:')
            afficher_depenses(depenses)
    
        elif choix == '3':
            print('\nTotal des dépenses: ', total_depenses(depenses))
    
        elif choix == '4':
            categorie = input('Entrez la catégorie à filtrer: ')
            print(f'\nDépenses pour {categorie}:')
            depenses_de_categorie = filtrer_depenses_par_categorie(depenses, categorie)
            afficher_depenses(depenses_de_categorie)
    
        elif choix == '5':
            print('Fin du programme.')
            break

# Lancement du programme
main()
