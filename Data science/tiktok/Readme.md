# Collecteur TikTok : Système de collecte automatisée de données pour analyse

Ce projet est un collecteur automatisé de données TikTok, conçu pour extraire régulièrement des informations publiques sur des vidéos associées à une liste de hashtags. L’objectif principal est de constituer une base de données structurée qui pourra ensuite être utilisée pour des analyses statistiques, des visualisations ou des études de tendances sur TikTok. Ce collecteur ne réalise pas d’analyse en temps réel : il se concentre sur la collecte, l’enregistrement et la mise à jour des données, qui seront exploitées ultérieurement.

Le script fonctionne en mode automatique : il interroge TikTok toutes les minutes pour chaque hashtag défini, récupère les informations principales des vidéos (auteur, description, likes, partages, commentaires, date de publication, URL), et les enregistre dans un fichier CSV. Les données sont ensuite automatiquement versionnées et synchronisées sur GitHub pour garantir leur sauvegarde et leur accessibilité.

## Fonctionnalités

- Collecte régulière des vidéos TikTok par hashtag
- Extraction des métadonnées principales de chaque vidéo
- Sauvegarde structurée dans un fichier CSV
- Commit et push automatique sur GitHub à chaque collecte
- Système entièrement automatisé (aucune intervention manuelle requise)

## Technologies et outils utilisés

- **Python 3** : langage principal du projet
- **TikTokApi** : bibliothèque pour accéder aux données publiques TikTok
- **asyncio** : gestion des appels asynchrones nécessaires à TikTokApi
- **pandas** : manipulation et sauvegarde des données au format CSV
- **schedule** : planification des tâches automatiques
- **git** : versionnement et synchronisation sur GitHub
- **playwright** : nécessaire pour TikTokApi (installation des navigateurs)

## Installation et prérequis

Avant d’exécuter le collecteur, installez les dépendances suivantes :

```bash
pip install TikTokApi pandas schedule playwright
playwright install