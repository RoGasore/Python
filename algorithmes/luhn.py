# Algorithme de Luhn 

def verifier_numero_carte(numero_carte):
    somme_impairs = 0
    numero_inverse = numero_carte[::-1]  
    chiffres_impairs = numero_inverse[::2]  

    for chiffre in chiffres_impairs:
        somme_impairs += int(chiffre)  

    # Somme des chiffres aux positions paires (à partir de la droite)
    somme_pairs = 0
    chiffres_pairs = numero_inverse[1::2] 

    for chiffre in chiffres_pairs:
        nombre = int(chiffre) * 2  # On double
        if nombre >= 10:  
            nombre = (nombre // 10) + (nombre % 10)
        somme_pairs += nombre

    # Total final
    total = somme_impairs + somme_pairs
    return total % 10 == 0  # Valide si divisible par 10


def main():
    numero_carte = '4001-1111-4555-1111'
    traduction = str.maketrans({'-': '', ' ': ''})  # Retirer tirets et espaces
    numero_sans_separateurs = numero_carte.translate(traduction)

    if verifier_numero_carte(numero_sans_separateurs):
        print('VALIDE')
    else:
        print('INVALIDE')


# Lancement du programme
main()
