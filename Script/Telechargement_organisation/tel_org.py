import os
import shutil
import yt_dlp
from mutagen.easyid3 import EasyID3

lien_playlist = "" #lien de la playlist

dossier_telechargement = "" #dossier de téléchargement
dossier_final = "" #dossier final

os.makedirs(dossier_telechargement, exist_ok=True)
os.makedirs(dossier_final, exist_ok=True)

#Fonction de progression
def progression(d) :
    if d['status'] == 'downloading' :
        print(f"Téléchargement : {d['_percent_str']} - {d['filename']}")
    elif d['status'] == 'finished':
        print(f"Téléchargement terminé : {d['filename']}")

options = {
    "format": "bestaudio/best",
    "outtmpl": f"{dossier_telechargement}/%(title)s.%(ext)s",
    "ignoreerrors" : True,
    "progress_hooks" : [progression],
    "postprocessors" : [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192"
    }],
    "download_archive" : "deja_telecharges.txt",
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([lien_playlist])

print("Organisation des musiques...")

# Organiser par artiste
for fichier in os.listdir(dossier_telechargement):
    if fichier.endswith(".mp3"):
        chemin = os.path.join(dossier_telechargement, fichier)
        artiste = "Inconnu"
        # Essayer d'obtenir l'artiste via les métadonnées
        try:
            audio = EasyID3(chemin)
            artiste_meta = audio.get("artist", [None])[0]
            if artiste_meta and artiste_meta.strip():
                artiste = artiste_meta.strip()
        except Exception:
            pass
        # Si pas de métadonnées, deviner via le nom du fichier
        if artiste == "Inconnu" and " - " in fichier:
            artiste = fichier.split(" - ")[0].strip()
        # Nettoyer le nom de l'artiste
        if not artiste:
            artiste = "Inconnu"
        dossier_artiste = os.path.join(dossier_final, artiste)
        os.makedirs(dossier_artiste, exist_ok=True)
        nouveau_chemin = os.path.join(dossier_artiste, fichier)
        if not os.path.exists(nouveau_chemin):
            shutil.move(chemin, nouveau_chemin)
            print(f"{fichier} déplacé vers {artiste}")
        else:
            os.remove(chemin)  # pour éviter des doublons
            print(f"Doublon trouvé et supprimé : {fichier}")

print("\nTout est prêt, ta playlist est bien rangée !")
