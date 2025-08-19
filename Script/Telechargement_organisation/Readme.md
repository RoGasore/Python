# Téléchargement et Organisation Automatique

Ce script Python permet de télécharger des fichiers (par exemple des vidéos ou de la musique) et de les organiser automatiquement dans des dossiers selon leur type ou leurs métadonnées. Il utilise les bibliothèques `yt-dlp` pour le téléchargement et `mutagen` pour la gestion des métadonnées audio.

## Fonctionnalités
- Téléchargement de vidéos ou musiques depuis des plateformes en ligne
- Organisation automatique des fichiers téléchargés dans des dossiers spécifiques
- Extraction et utilisation des métadonnées pour classer les fichiers audio

## Prérequis
Installez les dépendances nécessaires avec :
```powershell
pip install yt-dlp mutagen
```

## Utilisation
1. Modifiez les paramètres du script selon vos besoins (URL, dossier de destination, etc.).
2. Exécutez le script :
   ```powershell
   python tel_org.py
   ```
3. Les fichiers seront téléchargés et organisés automatiquement.

## Exemple de structure organisée
```
Telechargement_organisation/
├── Musique/
├── Vidéos/
├── tel_org.py
```

## Personnalisation
- Vous pouvez adapter le script pour organiser selon d'autres critères (date, artiste, genre, etc.).
- Ajoutez d'autres extensions ou types de fichiers selon vos besoins.

## Auteur
RoGasore

## Licence
Ce script est fourni à titre éducatif et peut être modifié selon vos besoins.
