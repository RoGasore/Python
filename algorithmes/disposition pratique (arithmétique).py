#cet algo permet de mettre en forme une liste de problèmes arithmétiques (addition et soustraction uniquement) pour les afficher verticalement (disposition pratique) et côte à côte, comme on le fait à l’école primaire.
  problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def calcul(number_1, number_2, operator): 
    if operator == '+': 
        result = int(number_1) + int(number_2)
    elif operator == '-':
        result = int(number_1) - int(number_2)
    else: 
        return "Error: Operator must be '+' or '-'."
    return result


def aff_result(numbers_1, numbers_2, operator, result_fin, key, dico_result):
    dico_result[key] = [numbers_1, numbers_2, operator, result_fin]
    return dico_result


def arithmetic_arranger(problems, show_answers=False):
    # Vérification du nombre de problèmes
    if len(problems) > 5:
        return "Error: Too many problems."

    dico_result = {}

    # Traitement des problèmes un par un
    for key, problem in enumerate(problems):
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid problem format."

        numbers_1, operator, numbers_2 = parts

        # Vérif opérateur
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Vérif chiffres
        if not numbers_1.isdigit() or not numbers_2.isdigit():
            return "Error: Numbers must only contain digits."

        # Vérif longueur
        if len(numbers_1) > 4 or len(numbers_2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calcul du résultat
        result_fin = calcul(numbers_1, numbers_2, operator)

        # Stockage dans ton dico
        aff_result(numbers_1, numbers_2, operator, result_fin, key, dico_result)

    # Maintenant on construit les lignes finales
    line1, line2, line3, line4 = [], [], [], []

    for key, (n1, n2, op, res) in dico_result.items():
        width = max(len(n1), len(n2)) + 2
        line1.append(n1.rjust(width))
        line2.append(op + n2.rjust(width - 1))
        line3.append("-" * width)
        if show_answers:
            line4.append(str(res).rjust(width))

    # Assemblage
    arranged = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3)
    if show_answers:
        arranged += "\n" + "    ".join(line4)

    return arranged


# Exemple
print(arithmetic_arranger(problems))
print()
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
