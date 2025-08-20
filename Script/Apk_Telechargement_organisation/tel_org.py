import os
import shutil
import yt_dlp
from mutagen.easyid3 import EasyID3

# Chemins compatibles Android/PC
def get_music_dirs():
    home = os.environ.get("HOME") or os.path.expanduser("~")
    music_dir = os.path.join(home, "Music", "test")
    org_dir = os.path.join(music_dir, "Org")
    os.makedirs(music_dir, exist_ok=True)
    os.makedirs(org_dir, exist_ok=True)
    return music_dir, org_dir

# Fonction de progression (peut être remplacée par le front)
def progression(d):
    if d.get('status') == 'downloading':
        print(f"Téléchargement : {d.get('_percent_str', '')} - {d.get('filename', '')}")
    elif d.get('status') == 'finished':
        print(f"Téléchargement terminé : {d.get('filename', '')}")

# Téléchargement d'une playlist YouTube
def telecharger_playlist(url):
    dossier_telechargement, _ = get_music_dirs()
    options = {
        "format": "bestaudio/best",
        "outtmpl": f"{dossier_telechargement}/%(title)s.%(ext)s",
        "ignoreerrors": True,
        "progress_hooks": [progression],
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }],
        "download_archive": os.path.join(dossier_telechargement, "deja_telecharges.txt"),
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

# Organisation des musiques par artiste
def organiser_musiques():
    dossier_telechargement, dossier_final = get_music_dirs()
    print("Organisation des musiques...")
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
