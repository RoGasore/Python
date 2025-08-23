# Projet Enquete.ipynb : Système de Filtrage et Visualisation Interactive

Ce projet est un prototype de Data Science conçu pour expérimenter la géolocalisation, le filtrage de données et la visualisation interactive. L’objectif principal est de créer un outil capable de filtrer et de visualiser des individus ou des points d’intérêt dans une zone géographique donnée. Bien que ce projet soit présenté sous forme de démonstration avec des données fictives, il illustre comment un système similaire pourrait être utilisé pour des enquêtes ou des analyses statistiques, par exemple pour identifier des personnes d’un certain âge, des étudiants, des centres de santé, ou toute autre catégorie pertinente dans une région donnée.

Pour cette démonstration, toutes les données sont générées de manière aléatoire à l’aide de la bibliothèque Faker, combinée à pandas pour la manipulation des données et random pour certaines valeurs aléatoires. Chaque entrée contient un nom, un âge, une position géographique (latitude et longitude), ainsi que des informations supplémentaires telles que le statut étudiant, la participation à l’armée ou l’existence d’un casier judiciaire. Ces données sont purement fictives et servent uniquement à illustrer le fonctionnement du système. Elles peuvent cependant être remplacées par des entrées utilisateur ou par de vraies bases de données dans un cadre légal et éthique.

Le projet est subdivisé en trois grandes parties. La première partie concerne la génération des données fictives, qui permet de créer un jeu de données représentatif pour tester le système. La deuxième partie est le filtrage, qui consiste à sélectionner les individus selon différents critères tels que l’âge, le statut étudiant, la participation à l’armée, le casier judiciaire et la distance à un point central donné. La dernière partie est l’affichage sur la carte. Pour cela, le projet utilise la bibliothèque Folium pour générer une carte interactive. Un cercle représente la zone de recherche autour d’un centre donné, et les individus filtrés sont indiqués par des marqueurs visuels sous forme de croix rouges, permettant de repérer immédiatement les points d’intérêt.

## Technologies utilisées

- Python 3 : langage principal du projet
- pandas : manipulation et gestion des données
- Faker : génération de données fictives
- random : valeurs aléatoires pour certaines colonnes
- geopy : calcul des distances géographiques
- folium : visualisation interactive sur carte


## Extensions possibles

Ce projet constitue une base de démonstration statistique et géographique, mais il peut être enrichi de nombreuses manières :
- Ajouter plus de critères de filtrage, par exemple la profession ou le centre de santé fréquenté, etc.
- Différencier les marqueurs selon les attributs des individus (couleurs, icônes).
- Intégrer des cartes thermiques (heatmaps) pour visualiser les zones “chaudes”.
- Transformer le prototype en une application interactive avec saisie des données par l’utilisateur.
- Connecter le système à une base de données réelle ou à des capteurs IoT pour des données en temps réel.

# Auteur
***Rodrigue Gasore***
