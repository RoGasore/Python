"""
Cet algo calcule la racine carrée d’un nombre positif en utilisant la méthode de bissection.
Elle itère pour réduire l’intervalle jusqu’à atteindre la précision souhaitée et retourne une approximation de la racine.
Peut être utilisée pour des exercices numériques ou calculs sans fonctions intégrées.
"""

def racine_carree_bisection(nombre, precision=1e-7, iterations_max=100):
    if nombre < 0:
        raise ValueError("La racine carrée d'un nombre négatif n'est pas définie dans les nombres réels")
    if nombre == 1:
        racine = 1
        print(f"La racine carrée de {nombre} est 1")
    elif nombre == 0:
        racine = 0
        print(f"La racine carrée de {nombre} est 0")
    else:
        bas = 0
        haut = max(1, nombre)
        racine = None
        
        for _ in range(iterations_max):
            milieu = (bas + haut) / 2
            carre_milieu = milieu**2

            if abs(carre_milieu - nombre) < precision:
                racine = milieu
                break
            elif carre_milieu < nombre:
                bas = milieu
            else:
                haut = milieu

        if racine is None:
            print(f"Échec de convergence après {iterations_max} itérations.")
        else:   
            print(f"La racine carrée de {nombre} est approximativement {racine}")
    
    return racine

N = 16
racine_carree_bisection(N)
