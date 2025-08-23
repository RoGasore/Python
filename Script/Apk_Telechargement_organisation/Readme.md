# RG : Application Android de téléchargement et organisation de musiques YouTube

Cette application Android, développée en Python avec KivyMD, permet de télécharger automatiquement les musiques d’une playlist YouTube et de les organiser dans des dossiers par artiste. L’interface est moderne, claire/sombre, et le processus est entièrement automatisé.

## Fonctionnalités

- Téléchargement des musiques d’une playlist YouTube (yt-dlp)
- Conversion automatique en MP3
- Organisation des fichiers dans des dossiers par artiste (mutagen pour lecture des métadonnées)
- Interface utilisateur moderne (KivyMD)
- Barre de progression, notifications et console intégrée

## Structure du projet

```
Apk_Telechargement_organisation/
├── app.py        # Front-end KivyMD (interface et logique utilisateur)
├── tel_org.py    # Backend (téléchargement et organisation des fichiers)
```

## Installation et compilation

### Prérequis

- **Python 3**
- **KivyMD** (`pip install kivymd`)
- **yt-dlp** (`pip install yt-dlp`)
- **mutagen** (`pip install mutagen`)
- **ffmpeg** (à installer sur le système)
- **Buildozer** (pour générer l’APK, nécessite Linux ou WSL)

### Compilation APK

1. Installez les dépendances Python et ffmpeg.
2. Placez-vous dans le dossier du projet.
3. Initialisez Buildozer :
   ```bash
   buildozer init
   ```
4. Modifiez le fichier `buildozer.spec` :
   - `title = RG`
   - `requirements = python3,kivy,kivymd,yt-dlp,mutagen`
5. Compilez l’APK :
   ```bash
   buildozer -v android debug
   ```
6. Installez l’APK sur votre appareil Android.

## Utilisation

- Entrez l’URL de la playlist YouTube dans l’application.
- Lancez le téléchargement et l’organisation.
- Retrouvez vos musiques rangées par artiste dans le dossier de destination.

## Auteur

Rodrigue Gasore

