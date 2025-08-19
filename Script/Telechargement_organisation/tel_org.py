import os
import shutil
import yt_dlp
from mutagen.easyid3 import EasyID3

lien_playlist = "https://www.youtube.com/playlist?list=PLkqz3S84Tw-ScF_rKV6RALfLaUbViE_VX&si=ZlzWp_pF245axsIW"

dossier_telechargement = "C:\\Users\\Rg\\Music\\test"
dossier_final = "C:\\Users\\Rg\\Music\\test\\Org"

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

#Organiser par artiste
for fichier in os.path.join(dossier_telechargement) :
    if fichier.endswith(".mp3") :
        chemin = os.path.join(dossier_telechargement, fichier)
        try: 
            audio = EasyID3(chemin)
            artiste = audio.get("artist", ["Inconnu"])[0].strip()
        except Exception :
            #si la chanson n'a pas de métadonnées, on essaie de deviner via "Artiste - titre"
            if " - " in fichier:
                artiste = fichier.split(" - ")[0]
            else:
                artiste = "Inconnu"
            
        dossier_artiste = os.path.join(dossier_final, artiste)
        os.makedirs(dossier_artiste, exist_ok=True)
        
        nouveau_chemin = os.path.join(dossier_artiste, fichier)
        if not os.path.exists(nouveau_chemin):
            shutil.move(chemin, nouveau_chemin)
            print(f"{fichier} déplacé vers {artiste}")
        else :
            os.remove(chemin) #pour eviter des doublons
            print(f"Doublon trouvé et supprimé : {fichier}")

print("\n Tout est pret, ta playlist est bien rangée !")
