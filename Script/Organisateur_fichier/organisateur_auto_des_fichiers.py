import os
import shutil
import sys

def barre_progression(actuel, total):
    pourcent = int((actuel / total) * 100)
    longueur_barre = 50
    nb_blocs = int((pourcent / 100) * longueur_barre)
    barre = '-' * nb_blocs + '-' * (longueur_barre - nb_blocs)
    sys.stdout.write(f"\rProgression: [{barre}] {pourcent}% ({actuel}/{total})")
    sys.stdout.flush()

dossier = "c:\\Users\\Rg\\Documents" # Dossier à organiser

categories = {
    "PDFs": [".pdf", ".PDF"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mov", ".m4a"],
    "Docs Word": [".doc", ".docx", ".txt"],
    "Feuilles": [".xls", ".xlsx", ".csv", ".ods"],
    "Presentations": [".ppt", ".pptx", ".odp"],
    "Musiques": [".mp3", ".wav", ".flac"],
    "Programmes": [".exe", ".msi", ".apk"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

# Créer les dossiers nécessaires
fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
total_fichiers = len(fichiers)
dossiers_utiles = set()
for truc in fichiers:
    ext = os.path.splitext(truc)[1].lower()
    for nom_cat, extensions in categories.items():
        if ext in [e.lower() for e in extensions]:
            dossiers_utiles.add(nom_cat)
            break
for nom_cat in dossiers_utiles:
    chemin = os.path.join(dossier, nom_cat)
    if not os.path.exists(chemin):
        os.makedirs(chemin)

for i, truc in enumerate(fichiers, 1):
    chemin_fichier = os.path.join(dossier, truc)
    ext = os.path.splitext(truc)[1].lower()
    for nom_cat, extensions in categories.items():
        if ext in [e.lower() for e in extensions]:
            shutil.move(chemin_fichier, os.path.join(dossier, nom_cat, truc))
            break
    barre_progression(i, total_fichiers)

print("\nOrganisation terminée.")