import os 

chemin = "R:\Python\Exercices python"
dossiers = os.path.join(chemin, "dossier", "tesr")
os.makedirs(dossiers, exist_ok=True)
